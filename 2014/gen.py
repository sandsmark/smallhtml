#!/usr/bin/python
from math import cos, sin, pi, ceil
from random import randint, random

htmlFile = open("small.html", "w")
htmlFile.write("<body>\n"
               "    <canvas id=\"canvas\" width=640 height=640 style=\"background:black\">\n"
               "    </canvas>\n"
               "    <script>\n"
               "        var canvas = document.getElementById('canvas');\n"
               "        var ctx = canvas.getContext('2d');\n"
               "        var data = [\n")

radii = []
angles = []
for i in range(100):
    radii.append(randint(0, 255))
    angles.append(random() * pi * 2)

for frame in range(0, 905):
    htmlFile.write("                       // Definition of a single particle at a discrete time step\n")
    htmlFile.write("                       [\n")
    for i in range(100):
        x = int(cos(angles[i]) * radii[i] + 320)
        y = int(sin(angles[i]) * radii[i] + 320)
        htmlFile.write("                           [\n"
                       "                               // X position of particle\n"
                       "                               " + str(x) + ",\n"
                       "                               // Y position of particle\n"
                       "                               " + str(y) + ",\n"
                       "                               // Color intensity of particle\n"
                       "                               " + str(radii[i]) + "\n"
                       "                           ],\n")
        if x > 640 or x < 0 or y > 640 or y < 0:
            radii[i] = 0
        else:
            radii[i] += 5
    htmlFile.write("                       ],\n")
htmlFile.write("                   ];\n")

htmlFile.write("        var index=0;\n"
               "        function drawshit() {\n"
               "            // Clear the canvas\n"
               "            canvas.width = canvas.width;\n"
               "            index++;\n"
               "            index %= 905;\n"
               "            for (var i=0; i<data[index].length; i++) {\n"
               "                ctx.fillStyle = \"rgb(\" + data[index][i][2] + \",\" + data[index][i][2] + \",\" + data[index][i][2] + \")\";\n"
               "                ctx.fillRect(data[index][i][0], data[index][i][1], 1, 1);\n"
               "            }\n"
               "        }\n"
               "        window.setInterval(drawshit, 50);\n")

htmlFile.write("    </script>\n"
               "</body>")
