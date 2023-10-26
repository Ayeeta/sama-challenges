import json


def checkTrianglesHasNoOcclusiveValues(json_data):
    count = 0
    for task in json_data["tasks"]:       
        for shape_group in task['answers']['Annotation']['layers']['vector_tagging']['shape_groups']:            
            for shape in shape_group['shapes']:
                if shape['type'] == 'polygon' and shape['tags'].get('Shape') == 'Triangle' and shape['tags'].get('Occlusion') is not None:
                    count += 1
    if count >= 1:
        return f'{count} Triangle(s) found. Triangle should not have occlusion values'            


def checkPointsHaveNoOcclusiveValues(json_data):
    for task in json_data["tasks"]:       
        for shape_group in task['answers']['Annotation']['layers']['vector_tagging']['shape_groups']:
            for shape in shape_group['shapes']:
                if shape['type'] == 'point' and 'Occlusion' in shape.get('tags', {}):
                    return 'Point should not have occlusion values'
    return 'No Point with occlusion values found'

        

def isTriangleGrouped(json_data):
    for task in json_data["tasks"]:       
        for shape_group in task['answers']['Annotation']['layers']['vector_tagging']['shape_groups']:
            for shape in shape_group['shapes']:            
                if shape['tags'].get('Shape') == 'Triangle':
                    return 'Triangles should not be grouped'    
    return 'No grouped Triangles'


def checkOneTriangleExists(json_data):
    triangle_count = 0
    for task in json_data["tasks"]:       
        for shape_group in task['answers']['Annotation']['layers']['vector_tagging']['shape_groups']:
            for shape in shape_group['shapes']:                
                if shape['type'] == 'polygon' and shape['tags'].get('Shape') == 'Triangle':
                    triangle_count += 1
    if triangle_count > 1:
        return 'There should be  one Triangle in a group'


def checkQuadShapeOrder(json_data):
    clockwise_order = ['Top_Left', 'Top_Right', 'Bottom_Right', 'Bottom_Left']
    for task in json_data["tasks"]:       
        for shape_group in task['answers']['Annotation']['layers']['vector_tagging']['shape_groups']:
            for shape in shape_group['shapes']:        
                if shape['type']== 'polygon' and shape['tags']['Shape'] == 'Quad':
                    if list(shape['tags']['Shape']['Occlusion'].keys()) == clockwise_order:
                        return json_data
    return 'Quard should be in clockwise order'        
        
    

def checkQuadShapeCorners(json_data):
    for task in json_data["tasks"]:       
        for shape_group in task['answers']['Annotation']['layers']['vector_tagging']['shape_groups']:    
            for shape in shape_group['shapes']:                
                if shape['type']== 'polygon' and shape['tags']['Shape'] == 'Quad':
                    for key_location in shape['key_locations']:
                        if len(key_location['points']) != 4:
                            return 'Quad should have 4 corners'
                        pass
                pass
    pass

def checkAGroupHasOneQuadAndOnePoint(json_data):
    for task in json_data["tasks"]:
        quad_count = 0
        point_count = 0
        for shape_group in task['answers']['Annotation']['layers']['vector_tagging']['shape_groups']:
            for shape in shape_group['shapes']:
                if shape['type'] == 'polygon' and shape['tags'].get('Shape') == 'Quad':
                    quad_count += 1
                if shape['type'] == 'point':
                    point_count += 1
            
            if quad_count != 1 or point_count != 1:
                return 'A group should have one Quad and one Point'
            
            quad_count = 0
            point_count = 0
    return 'Each group has exactly one Quad and one Point'


def validateJson(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)       
               
     
        # clockwise_order = checkQuadShapeOrder(json_data)
         
        print(f"""Validation failures:
            -{checkAGroupHasOneQuadAndOnePoint(json_data)} 
            -{checkOneTriangleExists(json_data)} 
            -{isTriangleGrouped(json_data)} 
            -{checkPointsHaveNoOcclusiveValues(json_data)} 
            -{checkTrianglesHasNoOcclusiveValues(json_data)} 
            -{checkQuadShapeCorners(json_data)}""")       

    except (json.JSONDecodeError, FileNotFoundError) as e:
        return 'Not Json file '+str(e)


validateJson('q2.json')