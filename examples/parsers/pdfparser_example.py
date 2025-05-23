#!/usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:quincy qiang
@license: Apache Licence
@file: pdfparser_example.py
@time: 2024/06/06
@contact: yanqiangmiffy@gamil.com
@software: PyCharm
@description: coding..
"""
from trustrag.modules.document.pdf_parser_fast import PdfParserUsingPyMuPDF


if __name__ == '__main__':
    parser=PdfParserUsingPyMuPDF(max_chunk_size=1000)
    # chunks=parser.parse(fnm="../../data/docs/汽车操作手册.pdf")
    # print(len(chunks))
    # for chunk in chunks:
    #     print(chunk)

    chunks = parser.parse(fnm="../../data/docs/5G垂直行业基础知识介绍--口袋小册子.pdf")
    print(chunks)
    print(len(chunks))
    for chunk in chunks:
        print(chunk)