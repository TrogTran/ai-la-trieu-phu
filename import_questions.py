import json
from pymongo import MongoClient
from pymongo.errors import PyMongoError

# Kết nối tới MongoDB
client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
db = client["login_data"]  # Tên database giống trong ứng dụng của bạn
questions_collection = db["questions_bank"]  # Tên collection

# Đọc file JSON
def load_questions_from_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            questions = json.load(file)
        return questions
    except FileNotFoundError:
        print(f"Không tìm thấy file {file_path}!")
        return []
    except json.JSONDecodeError:
        print("Lỗi định dạng JSON!")
        return []

# Hàm thêm câu hỏi từ file JSON
def insert_questions(questions):
    try:
        if questions:
            result = questions_collection.insert_many(questions)
            print(f"Đã thêm thành công {len(result.inserted_ids)} câu hỏi từ file JSON!")
        else:
            print("Không có câu hỏi nào để thêm!")
    except PyMongoError as e:
        print(f"Lỗi khi thêm câu hỏi: {str(e)}")

# Thực thi
if __name__ == "__main__":
    file_path = "questions.json"  # Đường dẫn tới file JSON
    questions_list = load_questions_from_json(file_path)
    insert_questions(questions_list)