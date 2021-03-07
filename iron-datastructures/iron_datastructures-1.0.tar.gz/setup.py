#!python3.9

from setuptools import setup  # type: ignore

setup(
    name="iron_datastructures",
    version="1.0",
    description="A set of useful data structures, including circular queue, binary tree/graph, linked list, and stack.",
    url="https://github.com/ntflix/iron_datastructures",
    author="Felix Weber",
    author_email="felix@iron59.co.uk",
    license="GNU GPLv3",
    package_data={
        "iron_datastructures": [
            "py.typed",
            "stack.pyi",
            "linked_list.pyi",
            "linked_list_node.pyi",
            "graph.pyi",
            "graph_node.pyi",
            "circular_queue.pyi",
            "_queue_position.pyi",
        ]
    },
    packages=["iron_datastructures"],
    zip_safe=False,
)
