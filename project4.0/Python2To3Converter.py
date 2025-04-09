import os
import re
import shutil
import subprocess
from pathlib import Path

class Python2To3Converter:
    def __init__(self, input_path, output_suffix="_py3"):
        self.input_path = Path(input_path).resolve()
        self.output_path = self._generate_output_path(output_suffix)
        self.temp_dir = Path.cwd() / "__temp__"  # 固定临时目录位置

    def _generate_output_path(self, suffix):
        """生成输出文件路径（与原文件同目录）"""
        return self.input_path.parent / f"{self.input_path.stem}{suffix}{self.input_path.suffix}"

    def convert(self):
        """执行安全转换（不修改源文件）"""
        try:
            # 确保临时目录存在且为空
            self._prepare_temp_dir()

            # 复制源文件到临时目录
            temp_input = self.temp_dir / self.input_path.name
            shutil.copy(self.input_path, temp_input)

            # Step 1: 在临时目录运行 2to3
            self._run_2to3(temp_input)

            # Step 2: 读取转换后内容
            converted_content = self._read_converted_content(temp_input)

            # Step 3: 应用自定义修复
            final_content = self._apply_custom_fixes(converted_content)

            # Step 4: 写入最终输出文件
            self._write_final_output(final_content)

            print(f"转换成功！输出文件: {self.output_path}")
        except Exception as e:
            print(f"转换失败: {str(e)}")
        finally:
            # 无论成功与否，强制删除临时目录
            self._cleanup_temp_dir()

    def _prepare_temp_dir(self):
        """创建或清空临时目录"""
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)
        self.temp_dir.mkdir(parents=True)

    def _run_2to3(self, temp_input):
        """在临时目录运行 2to3"""
        try:
            subprocess.run(
                ["2to3", "--write", "--nobackups", "--output-dir", str(self.temp_dir), str(temp_input)],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr.decode() if e.stderr else "Unknown error"
            raise RuntimeError(f"2to3 转换失败: {error_msg}")

    def _read_converted_content(self, temp_input):
        """读取转换后的内容"""
        converted_file = self.temp_dir / temp_input.name
        if not converted_file.exists():
            raise FileNotFoundError("2to3 未生成转换文件")
        return converted_file.read_text(encoding="utf-8")

    def _apply_custom_fixes(self, content):
        """应用自定义修复规则"""
        fixes = [
            self._fix_selenium_methods,
            self._fix_switch_to_alert,
            self._remove_unicode_prefix,
            self._add_by_import,
            self._remove_executable_path,
            self._change_base_url,
            self._add_chrome_options
        ]
        for fix in fixes:
            content = fix(content)
        return content

    def _write_final_output(self, content):
        """写入最终输出文件"""
        self.output_path.write_text(content, encoding="utf-8")

    def _cleanup_temp_dir(self):
        """强制删除临时目录"""
        if self.temp_dir.exists():
            try:
                shutil.rmtree(self.temp_dir)
            except Exception as e:
                print(f"警告: 临时目录清理失败 - {str(e)}")

    # ------------ 自定义修复规则（保持不变）------------
    def _fix_selenium_methods(self, content):
        return re.sub(
            r"\.find_element_by_(\w+)\((.*?)\)",
            lambda m: f".find_element(By.{m.group(1).upper()}, {m.group(2)})",
            content,
            flags=re.IGNORECASE
        )

    def _fix_switch_to_alert(self, content):
        return content.replace("switch_to_alert()", "switch_to.alert")

    def _remove_unicode_prefix(self, content):
        return re.sub(r'u"([^"]*)"', r'"\1"', content)

    def _add_by_import(self, content):
        if "from selenium.webdriver.common.by import By" not in content:
            return content.replace(
                "from selenium import webdriver",
                "from selenium import webdriver\nfrom selenium.webdriver.common.by import By"
            )
        return content

    def _remove_executable_path(self, content):
        return re.sub(
            r"self\.driver\s*=\s*webdriver\.Chrome\(executable_path=(?:r?\'|\"|\()(.*?)(?:\'|\"|\))\)",
            r"self.driver = webdriver.Chrome()",
            content
        )
    
    def _change_base_url(self, content):
        return content.replace('self.base_url = "https://www.google.com/"', 'self.base_url = "https://cn.bing.com/"')

    def _add_chrome_options(self, content):
        chrome_options_code = """
        # 设置ChromeOptions，防止浏览器自动关闭
        options = Options()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)
        """
        # 查找 self.driver = webdriver.Chrome() 并替换为带有 options 的版本
        content = re.sub(
            r"self\.driver\s*=\s*webdriver\.Chrome\(\)",
            chrome_options_code.strip(),
            content
        )
        
        # 确保导入 Options 类
        if "from selenium.webdriver.chrome.options import Options" not in content:
            content = content.replace(
                "from selenium import webdriver",
                "from selenium import webdriver\nfrom selenium.webdriver.chrome.options import Options"
            )
        
        return content
# if __name__ == "__main__":
#     # 使用示例
#     converter = Python2To3Converter(
#         input_path="D:/vscodeproject/python/project4.0/UntitledTestCase.py",
#         output_suffix="_converted"
#     )
#     converter.convert()
#     print("Finish")