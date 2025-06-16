import re
import json


def convert_code_to_json(code):
    # 按函数分割代码
    function_blocks = re.split(r'\n\s*\n', code.strip())
    result = {}

    for block in function_blocks:
        lines = block.split('\n')
        if not lines:
            continue

        # 解析函数名和参数
        func_match = re.match(r'^\s*(\w+)\s*\((.*?)\)\s*\{', lines[0])
        if not func_match:
            continue

        func_name = func_match.group(1)
        func_body = []

        # 处理函数体内的每一行
        for line in lines[1:]:
            line = line.strip()
            # 跳过空行和注释
            if not line or line.startswith('#'):
                continue

            # 移除行尾注释
            if '#' in line:
                line = line.split('#')[0].strip()

            # 匹配函数调用 (如 init(3))
            call_match = re.match(r'^\s*(\w+)\s*\((.*?)\)\s*$', line)
            if call_match:
                func_called = call_match.group(1)
                args = call_match.group(2).split(',')
                call_dict = {"func": func_called}

                for i, arg in enumerate(args, start=1):
                    arg = arg.strip()
                    # 处理字符串参数 (如 "3")
                    if re.match(r'^".*"$', arg):
                        call_dict[f"v{i}"] = ["str", arg.strip('"')]
                    # 处理整型参数
                    elif arg.isdigit():
                        call_dict[f"v{i}"] = ["int", int(arg)]
                    # 处理变量参数
                    else:
                        call_dict[f"v{i}"] = ["var", arg]

                func_body.append(call_dict)
                continue

            # 匹配赋值语句 (如 a=3 或 b="3")
            assign_match = re.match(r'^\s*(\w+)\s*=\s*(.*?)\s*$', line)
            if assign_match:
                var_name = assign_match.group(1)
                value = assign_match.group(2).strip()

                # 处理字符串赋值
                if re.match(r'^".*"$', value):
                    value_info = ["str", value.strip('"')]
                # 处理整型赋值
                elif value.isdigit():
                    value_info = ["int", value]  # 保留字符串形式
                else:
                    value_info = ["var", value]  # 处理变量赋值

                func_body.append([var_name, "=", value_info])

        result[func_name] = func_body

    return result


# 测试代码
if __name__ == "__main__":
    code = """
main(){
    init(3)  #注释
    a=3
    b="3"
}

init(x){
    print(x, "!")
    #注释
}
"""

    result = convert_code_to_json(code)
    print(json.dumps(result, indent=4))