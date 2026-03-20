from flask import Flask, render_template, request, jsonify
import json
import os
import Kernel_Calculate  # 匯入您原有的計算模組

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# 新增計算 API 接口
@app.route('/api/calculate', methods=['POST'])
def calculate():
    try:
        # 接收網頁傳來的工項資料
        work_item = request.json
        work_item_type = work_item.get("workItemType") # 區分是 Main Structure 或其他

        # 直接呼叫原有的 Kernel_Calculate.calDetail 函式
        # 該函式會回傳 list[list]，例如 [["1.102", "結構用...", "=", "1.25", "m3"], ...]
        detail_result = Kernel_Calculate.calDetail(work_item_type, work_item)

        return jsonify({
            "status": "success",
            "detail": detail_result
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

# 產生 JSON 的 API (用於最後導出)
@app.route('/api/save_json', methods=['POST'])
def save_json():
    try:
        data = request.json
        # 這裡的 data 預期包含 { workItemsDict, caculateDataDict, caseData }
        # 比照 DesignHelper.py 的儲存格式
        print(data)
        output_format = [
            data.get('workItemsDict', {}),
            data.get('caculateDataDict', {}),
            data.get('caseData', {})
        ]
        print(output_format)
        json_str = json.dumps(output_format, ensure_ascii=False, indent=2)
        return jsonify({"status": "success", "json_str": json_str})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

# localhost:5000