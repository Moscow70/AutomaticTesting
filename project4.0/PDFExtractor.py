import fitz  # PyMuPDF

class PDFExtractor:
    def __init__(self, file_path):
        """
        初始化 PDFExtractor 类。
        :param file_path: PDF 文件的路径。
        """
        self.file_path = file_path

    def extract_content(self):
        """
        分段提取文档内容，确保表格不被硬性分段隔断。
        :return: 返回一个列表，每个元素是字典：
                 - 'type': 'text' 或 'table'
                 - 'data': 文本段落或表格数据（二维列表）
        """
        try:
            doc = fitz.open(self.file_path)
            all_content = []

            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                page_content = self._process_page(page)
                all_content.extend(page_content)

            return all_content

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def _process_page(self, page):
        """
        处理单个页面，提取并整合文本和表格内容。
        :param page: fitz.Page 对象
        :return: 页面内容列表，包含交替的文本段落和完整表格
        """
        # 提取页面中的表格及其边界框
        tables = page.find_tables()
        table_data = []
        table_bboxes = []
        for table in tables:
            table_data.append(table.extract())
            table_bboxes.append(table.bbox)  # 表格的坐标 (x0, y0, x1, y1)

        # 提取文本块（排除表格区域）
        text_blocks = page.get_text("blocks")
        filtered_blocks = []
        for block in text_blocks:
            block_rect = fitz.Rect(block[:4])  # 文本块的坐标 (x0, y0, x1, y1)
            is_inside_table = any(block_rect.intersects(fitz.Rect(t_bbox)) for t_bbox in table_bboxes)
            if not is_inside_table and block[4].strip():  # 过滤空白块
                filtered_blocks.append(block[4].strip())

        # 按位置排序元素（文本和表格）
        elements = []
        # 添加表格元素
        for data in table_data:
            elements.append({"type": "table", "data": data})
        # 添加文本元素（合并为段落）
        if filtered_blocks:
            elements.append({"type": "text", "data": "\n".join(filtered_blocks)})

        return elements

# # 示例用法
# if __name__ == "__main__":
#     extractor = PDFExtractor("simplified_document.pdf")
#     content = extractor.extract_content()

#     if content:
#         for item in content:
#             if item["type"] == "text":
#                 print("文本段落:")
#                 print(item["data"])
#                 print("-" * 50)
#             elif item["type"] == "table":
#                 print("表格内容:")
#                 for row in item["data"]:
#                     print(row)
#                 print("-" * 50)