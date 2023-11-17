import csv
import re


def csv_to_html(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        data = list(csvreader)

    html = "\t"+"<tr>"+"\n"
    row = data[0]
    for i in range(len(row)):
        html += "\t"+"\t"+f"<td>{row[i]}</td>"+"\n"
    html += "\t"+"</tr>"+"\n" 
    for row in data[1:]:
        html += "\t"+"<tr>"+"\n"
        for i in range(len(row)):
            if i == 3:
                html += "\t"+"\t"+f"<td><a href=\"https://www.rfc-editor.org/info/rfc{row[i]}\">{row[i]}</a></td>"+"\n"
            else:
                html += "\t"+"\t"+f"<td>{row[i]}</td>"+"\n"
        html += "\t"+"</tr>"+"\n"

    with open(output_file, 'w', encoding='utf-8') as htmlfile:
        htmlfile.write(html)
    return html

input_file = 'data.csv'  # 替换为你的CSV文件路径
output_file = 'data.html'  # 输出的HTML文件名

table_content = csv_to_html(input_file, output_file)


# 读取 HTML 文件  
with open('../content/rfcs/index.md', 'r', encoding='utf-8') as file:  
    html_content = file.read()

# 匹配<table>标签及其内容  
table_pattern = r'<table id=myTable>(.*?)</table>'
# 查找所有匹配项  
table_matches = re.findall(table_pattern, html_content, re.DOTALL)

html_content = html_content.replace(table_matches[0], table_content)

# 重新将修改后的 HTML 内容写入文件  
with open('../content/rfcs/index.md', 'w', encoding='utf-8') as file:  
    file.write(html_content)

print("replaced content of rfc page")
