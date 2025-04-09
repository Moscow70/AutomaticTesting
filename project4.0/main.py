from PDFExtractor import PDFExtractor
from SmartTableExtractor import SmartTableExtractor
import json
from pathlib import Path
from LLMTextFilter import LLMTextFilter
from KatalonAIAssistant import AdvancedCodeAnnotator
from Python2To3Converter import Python2To3Converter
from AICodeGnerator import AICodeGenerator

def main():
    # 指定 PDF 文件的绝对路径（替换为你的实际路径）
    pdf_path = "D:/workspace/originalfiles/CASC-STEC-PT011能力验证统软件需求规格说明_用户管理.pdf"

    try:
        # # ========== 第一阶段：提取原始内容 ==========
        # pdf_extractor = PDFExtractor(pdf_path)
        # raw_content = pdf_extractor.extract_content()
        
        # if not raw_content:
        #     print("内容提取失败")
        #     return

        # # 分离文本段落
        # text_segments = [item["data"] for item in raw_content if item["type"] == "text"]

        # # 分离表格
        # table_segments = [item["data"] for item in raw_content if item["type"] == "table"]

        # #将table_segments导出到文本文件
        # with open("D:/workspace/originalfiles/table_segments.txt", "w", encoding="utf-8") as f:
        #     for table in table_segments:
        #         f.write(json.dumps(table, ensure_ascii=False) + "\n\n")

        # table_extractor = SmartTableExtractor()

        # try:    
        #     # 提取约束信息
        #     constraints = table_extractor.extract_constraints(table_segments)
        #     output_path = "D:/vscodeproject/python/project4.0/constraints.json"
        #     with open(output_path, "w", encoding="utf-8") as f:
        #         json.dump(constraints, f, indent=2, ensure_ascii=False)
        #     print(f"\n✅ 约束条件已保存至：{output_path}")
            
        #     # 打印结果
        #     # print("="*50 + " 提取结果 " + "="*50)
        #     # print(json.dumps(constraints, indent=2, ensure_ascii=False))
        #     print("="*50 + " 完成 " + "="*50)
    
        # except Exception as e:
        #     print("\n❌ 处理过程中发生错误:")
        #     print(f"错误类型: {type(e).__name__}")
        #     print(f"详细信息: {str(e)}")
        #     print("="*50 + " 错误 " + "="*50)
        
        # # ========== 第二阶段：文本清洗 ==========
        # llm_filter = LLMTextFilter()
        # cleaned_texts = llm_filter.filter_all_texts(text_segments)
        
        # # ========== 第三阶段：输出结果 ==========
        # print("\n" + "="*50 + " 清洗后的技术需求 " + "="*50)
        # for idx, text in enumerate(cleaned_texts, 1):
        #     if text:  # 跳过空结果
        #         print(f"\n🔧 技术需求 {idx}:")
        #         print("-" * 30)
        #         print(text)
        #         print("-" * 30)
                
        # print("="*50 + " 处理完成 " + "="*50 + "\n")

        # ========== 第四阶段：代码分析 ==========
        # katalon_script_path = "D:/vscodeproject/python/project4.0/UntitledTestCase.py"
        annotated_script_path = "D:/vscodeproject/python/project4.0/annotated_test.py"
        # print("\n" + "="*50 + " 开始代码转换 " + "="*50)
        
        # # 验证Katalon脚本存在
        # if not Path(katalon_script_path).exists():
        #     raise FileNotFoundError(f"Katalon脚本不存在: {katalon_script_path}")
        
        # # 将代码转换为python3格式
        # converter = Python2To3Converter(katalon_script_path, output_suffix="_converted")
        # converter.convert()
        # print("\n" + "="*50 + " 代码转换完成 " + "="*50)

        # converted_script_path = katalon_script_path.replace(".py", "_converted.py")

        # print("\n" + "="*50 + " 开始代码注释 " + "="*50)        
        # # 初始化注释器
        # annotator = AdvancedCodeAnnotator(
        #     constraints=constraints,  # 使用从PDF提取的约束
        #     chunk_size=4000
        # )
        
        # # 执行代码注释
        # try:
        #     annotator.annotate_file(converted_script_path, annotated_script_path)
        #     print(f"\n✅ 代码注释完成")
        #     print(f"输入文件: {converted_script_path}")
        #     print(f"输出文件: {annotated_script_path}")
            
        #     # 验证输出文件
        #     if Path(annotated_script_path).exists():
        #         print(f"生成文件大小: {Path(annotated_script_path).stat().st_size} 字节")
        #     else:
        #         print("⚠️ 输出文件未成功生成")
                
        # except Exception as e:
        #     print(f"\n❌ 代码注释失败: {str(e)}")
        
        # print("="*50 + " 处理完成 " + "="*50 + "\n")

        # ========== 第五阶段：修改代码 ==========
        new_script_path = "D:/vscodeproject/python/project4.0/modified_test.py"
        print("\n" + "="*50 + " 开始代码修改 " + "="*50)

        # 从本地文件读取约束条件
        constraints_path = "D:/vscodeproject/python/project4.0/constraints.json"
        with open(constraints_path, "r", encoding="utf-8") as f:
            file_constraints = json.load(f)

        # 初始化代码生成器
        generator = AICodeGenerator(
            constraints=file_constraints,  # 使用从PDF提取的约束
            chunk_size=4000
        )

        # 执行代码生成
        try:
            generator.annotate_file(annotated_script_path, new_script_path)
            print(f"\n✅ 代码修改完成")
            print(f"输入文件: {annotated_script_path}")
            print(f"输出文件: {new_script_path}")

            # 验证输出文件
            if Path(new_script_path).exists():
                print(f"生成文件大小: {Path(new_script_path).stat().st_size} 字节")
            else:
                print("⚠️ 输出文件未成功生成")
        
        except Exception as e:
            print(f"\n❌ 代码修改失败: {str(e)}")


    except Exception as e:
        print(f"程序运行异常: {e}")




if __name__ == "__main__":
    main()