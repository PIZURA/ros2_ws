import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def cb(request, response):
    if request.name == "山口 敦志":
        response.age = 19
    else:
        response.age = 255

    return response

rclpy.init()
node = Node("talker")
pub = node.create_service(Query, "query", cb)
rclpy.spin(node)
