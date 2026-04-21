from flask import Flask,request,jsonify
from services.algorithm_service import SortService

app = Flask(__name__)

#Serviceインスタンス
service = SortService()

@app.route("/")
def home():
    return {"message": "Sort API is running"}

@app.route("/sort",methods = ["POST"])
def sort():
    try:
        #JSONデータの取得
        req = request.get_json()
        
        data = req.get("data")
        algorithm = req.get("algorithm")
        
        #入力チェック
        if not isinstance(data,list):
            return jsonify({"error":"data must be a list"}),400
        
        if not isinstance(algorithm,str):
            return jsonify({"error":"algorithm must be a string"}),400
        
        algorithm = algorithm.lower()
        
        #ソート実行
        sorted_data = service.sort(data,algorithm)
        
        return jsonify({"sorted": sorted_data})
    
    except ValueError as e:
        return jsonify({"error": str(e)}),400
    
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}),500
    
if __name__ == '__main__':
    app.run(debug = True,port=5000)