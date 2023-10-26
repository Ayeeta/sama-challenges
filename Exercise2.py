import json


class JsonValidator:
    def __init__(self, json_data):
        self.shapes = []
        for task in json_data["tasks"]:
            for shape_group in task['answers']['Annotation']['layers']['vector_tagging']['shape_groups']:
                self.shapes.extend(shape_group['shapes'])

    def checkTrianglesHasNoOcclusiveValues(self):
        triangle_count = sum(1 for shape in self.shapes if shape['type'] == 'polygon' and
                             shape['tags'].get('Shape') == 'Triangle' and shape['tags'].get('Occlusion') is not None)
        if triangle_count >= 1:
            return f'{triangle_count} Triangle(s) found. Triangle should not have occlusion values'
        return None

    def checkPointsHaveNoOcclusiveValues(self):
        point_with_occlusion = any(shape['type'] == 'point' and 'Occlusion' in shape.get('tags', {}) for shape in self.shapes)
        if point_with_occlusion:
            return 'Point should not have occlusion values'
        return 'No Point with occlusion values found'

    def isTriangleGrouped(self):
        triangle_grouped = any(shape['tags'].get('Shape') == 'Triangle' for shape in self.shapes)
        if triangle_grouped:
            return 'Triangles should not be grouped'
        return 'No grouped Triangles'

    def checkOneTriangleExists(self):
        triangle_count = sum(1 for shape in self.shapes if shape['type'] == 'polygon' and shape['tags'].get('Shape') == 'Triangle')
        if triangle_count > 1:
            return 'There should be one Triangle in a group'
        return None

    def checkQuadShapeOrder(self):
        clockwise_order = ['Top_Left', 'Top_Right', 'Bottom_Right', 'Bottom_Left']
        for shape in self.shapes:
            if shape['type'] == 'polygon' and shape['tags'].get('Shape') == 'Quad':
                if list(shape['tags']['Occlusion'].keys()) != clockwise_order:
                    return 'Quad should be in clockwise order'
        return None

    def checkQuadShapeCorners(self):
        for shape in self.shapes:
            if shape['type'] == 'polygon' and shape['tags'].get('Shape') == 'Quad':
                for key_location in shape['key_locations']:
                    if len(key_location['points']) != 4:
                        return 'Quad should have 4 corners'
        return None

    def checkAGroupHasOneQuadAndOnePoint(self):
        quad_count = sum(1 for shape in self.shapes if shape['type'] == 'polygon' and shape['tags'].get('Shape') == 'Quad')
        point_count = sum(1 for shape in self.shapes if shape['type'] == 'point')
        if quad_count != 1 or point_count != 1:
            return 'Each group should have one Quad and one Point'
        return None



def validateJson(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)       
               
     
        # clockwise_order = jsonValidator.checkQuadShapeOrder()
        jsonValidator = JsonValidator(json_data) 

        print(f"""Validation failures:
            -{jsonValidator.checkAGroupHasOneQuadAndOnePoint()} 
            -{jsonValidator.checkOneTriangleExists()} 
            -{jsonValidator.isTriangleGrouped()} 
            -{jsonValidator.checkPointsHaveNoOcclusiveValues()} 
            -{jsonValidator.checkTrianglesHasNoOcclusiveValues()} 
            -{jsonValidator.checkQuadShapeCorners()}""")       

    except (json.JSONDecodeError, FileNotFoundError) as e:
        return 'Not Json file '+str(e)


validateJson('q2.json')