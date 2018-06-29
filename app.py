# -*- coding: utf-8 -*-

import re
from hashlib import md5

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/md5", methods=["POST"])
def calculate_md5():
    form_header = request.headers.get("Content-Type")
    app.logger.info(form_header)
    boundary = re.match("multipart/form-data; boundary=(.*)",
                        form_header).group(1).encode()

    inbody = False
    app.logger.info(boundary)
    chunk_size = 200
    md5_computer = md5()

    while True:
        chunk = request.stream.read(chunk_size)
        print(chunk)
        if len(chunk) == 0:
            break

        try:
            index = chunk.index(boundary)
        except ValueError:
            if inbody:
                md5_computer.update(chunk)
        else:
            if not inbody:
                # start
                app.logger.info("found boundary.")
                app.logger.info(f"First chunk orignal: {chunk}")
                inbody = True
                chunk = chunk.split(b'\r\n\r\n')[1]
                app.logger.info(f"First chunk: {chunk}")
                md5_computer.update(chunk)
            else:
                app.logger.info("out of boundary.")
                app.logger.info(f"Last chunk orignal: {chunk}")
                inbody = False
                chunk = chunk[:index-4]
                app.logger.info(f"Last chunk: {chunk}")
                md5_computer.update(chunk)
                return md5_computer.hexdigest()
