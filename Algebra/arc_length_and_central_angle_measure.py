def length_of_arc_function(ra,angle,type="degree"):
    import math
    if type == "degree":
        return ra*angle*math.pi/180
    elif type == "radians":
        return ra*angle

