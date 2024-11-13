from PIL import Image
import pytesseract

import os
from spire.pdf.common import *
from spire.pdf import *
import pytesseract
from PIL import Image

class image_extraction:

    def __init__(self, pdf_path, output_dir):
        self.pdf_path = pdf_path
        self.output_dir = output_dir

    def get_file_type(self):
        _, file_extension = os.path.splitext(self.pdf_path)
        file_extension = file_extension.lower()
        if file_extension == '.pdf':
            return 'pdf'
        else :
            return 'unknown'

    def extracting_image(self):
        """
        从PDF中提取所有图片，并将其保存到指定的输出目录中
        参数：
            pdf_path(str)：输入路径
            output_dir(str): 输出路径
        """
        if self.get_file_type() == 'pdf':
            print("PDF files can be extracted!")
        else:
            print("File Type Error!")
            return False

        doc = PdfDocument()
        doc.LoadFromFile(self.pdf_path)

        image_helper = PdfImageHelper()

        image_count = 1

        for page_index in range(doc.Pages.Count):
            page = doc.Pages[page_index]
            # 获取页面信息
            image_infos = image_helper.GetImagesInfo(page)

            # 提取并保存
            for image_index in range(len(image_infos)):
                # 指定输出文件
                output_file = os.path.join(self.output_dir, f"Image-{image_count}.png")
                # 保存为图片文件
                image_infos[image_index].Image.Save(output_file)
                image_count += 1
            
        doc.Close()
        print("Extracting Image Complete!")

    # def run(self):
    #     self.extract_images_from_pdf("D:/workspace/中国电信自研产品预集成测试-算力服务平台OPS操作手册（运维手册）_V0.1_20240517.pdf", "D:/workspace/image")

    #     try:
    #         image = Image.open('D:/workspace/image/Image-8.png')
    #         text = pytesseract.image_to_string(image, lang='chi_sim')

    #         with open('D:/workspace/output.txt', 'w') as f:
    #             f.write(text)
    #     except Exception as e:
    #         print("No image detected")
    #     else :
    #         print("Image detected")
