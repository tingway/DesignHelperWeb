from flask import Flask, render_template, request, jsonify, send_file
import json
import os
import io

app = Flask(__name__)

@app.route('/')
def index():
    # 渲染 template 資料夾下的 index.html
    return render_template('index.html')

@app.route('/api/save_json', methods=['POST'])
def save_json():
    try:
        data = request.json
        # 根據 DesignHelper.py 的資料結構組合輸出格式
        # 索引 0: workItemsDict, 1: caculateDataDict, 2: caseData
        output_format = [{}, {}, data]

        # 建立一個記憶體中的檔案物件，方便讓使用者下載，不一定要存存在 Render 伺服器硬碟
        json_str = json.dumps(output_format, ensure_ascii=False, indent=2)
        return jsonify({"status": "success", "data": output_format, "json_str": json_str})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    # Render 會自動分配 PORT
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)