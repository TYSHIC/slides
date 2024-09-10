import os
from PyPDF2 import PdfReader

def get_pdf_page_count(folder_path):
    # 初始化总页数变量
    total_pages = 0
    
    # 获取文件夹中所有PDF文件的路径
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

    # 遍历每个PDF文件并获取页数
    for pdf_file in pdf_files:
        file_path = os.path.join(folder_path, pdf_file)
        with open(file_path, 'rb') as f:
            pdf_reader = PdfReader(f)
            page_count = len(pdf_reader.pages)
            total_pages += page_count  # 累加页数
            print(f"{pdf_file}: {page_count} 页")

    # 返回总页数
    return total_pages

# 指定文件夹路径
folder_path = "./"  # 替换为您的PDF文件夹路径

# 获取PDF文件的页数
total_pages_in_folder = get_pdf_page_count(folder_path)
print(f"文件夹中所有PDF文件的总页数为: {total_pages_in_folder} 页")