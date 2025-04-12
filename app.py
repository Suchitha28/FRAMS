# from flask import Flask, render_template, request, redirect, url_for
# import os
# import cv2
# from datetime import datetime

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'static/uploads/profile_photos'
# app.config['DATASET_FOLDER'] = 'static/uploads/dataset'

# # Ensure upload folders exist
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
# os.makedirs(app.config['DATASET_FOLDER'], exist_ok=True)

# @app.route('/')
# def home():
#     return redirect(url_for('register'))

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         employee_name = request.form['employee_name']
#         user_id = request.form['user_id']
#         email = request.form['email']
#         phone = request.form['phone']

#         # Save profile photo
#         profile_photo = request.files['profile_photo']
#         photo_filename = f"{user_id}_{profile_photo.filename}"
#         profile_photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo_filename)
#         profile_photo.save(profile_photo_path)

#         # Save captured camera images
#         save_captured_images(user_id)

#         return f"✅ Registration successful for {employee_name}!"

#     return render_template('register.html')

# def save_captured_images(user_id):
#     dataset_path = os.path.join(app.config['DATASET_FOLDER'], user_id)
#     os.makedirs(dataset_path, exist_ok=True)

#     # We assume 50 captured images will be sent later (handled separately)
#     # Here you can simulate saving dummy images if needed.
#     print(f"[INFO] Placeholder: Saving captured images for {user_id}")

# if __name__ == '__main__':
#     app.run(debug=True)



# ....................... code 1....................
# from flask import Flask, render_template, request, redirect, url_for
# import os

# app = Flask(__name__)

# # Set up a folder to store profile photos and captured images
# app.config['UPLOAD_FOLDER'] = 'uploads/profile_photos'
# app.config['DATASET_FOLDER'] = 'uploads/dataset'

# # Ensure folders exist
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
# os.makedirs(app.config['DATASET_FOLDER'], exist_ok=True)

# @app.route('/')
# def home():
#     return redirect(url_for('register'))

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         employee_name = request.form['employee_name']
#         user_id = request.form['user_id']
#         email = request.form['email']
#         phone = request.form['phone']
        
#         profile_photo = request.files['profile_photo']
        
#         if profile_photo:
#             profile_photo_filename = f"{user_id}_profile.jpg"
#             profile_photo_path = os.path.join(app.config['UPLOAD_FOLDER'], profile_photo_filename)
#             profile_photo.save(profile_photo_path)

#         # Save employee details into a simple text file (later can upgrade to database)
#         employee_info = f"{employee_name},{user_id},{email},{phone},{profile_photo_filename}\n"
#         with open('employees.txt', 'a') as f:
#             f.write(employee_info)

#         return "✅ Registration Successful! Now you can proceed to attendance system."
#     return render_template('register.html')

# @app.route('/upload_captured_images', methods=['POST'])
# def upload_captured_images():
#     user_id = request.form.get('user_id')
#     dataset_path = os.path.join(app.config['DATASET_FOLDER'], user_id)
#     os.makedirs(dataset_path, exist_ok=True)

#     files = request.files.getlist('images')
#     for idx, file in enumerate(files):
#         filename = f"{user_id}_{idx}.jpg"
#         file.save(os.path.join(dataset_path, filename))

#     return "Captured images uploaded successfully!", 200

# if __name__ == '__main__':
#     app.run(debug=True)


# ........... code 2..................
# from flask import Flask, render_template, request, redirect, url_for
# import os

# app = Flask(__name__, static_folder='static', template_folder='templates')

# # Paths
# app.config['UPLOAD_FOLDER'] = 'uploads/profile_photos'
# app.config['DATASET_FOLDER'] = 'uploads/dataset'

# # Ensure folders exist
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
# os.makedirs(app.config['DATASET_FOLDER'], exist_ok=True)

# # -----> Home Route (Login Page First)
# @app.route('/')
# def home():
#     return render_template('login.html')

# # -----> New: Home page after login
# @app.route('/home')
# def homepage():
#     return render_template('home.html')

# # -----> Login Logic
# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form['username']
#     password = request.form['password']

#     # Example: basic check (you can connect DB later)
#     if username == "Rahul" and password == "Rahul123":
#         return redirect(url_for('home'))
#     else:
#         return "❌ Invalid credentials!"

# # -----> Registration Page
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         employee_name = request.form['employee_name']
#         user_id = request.form['user_id']
#         email = request.form['email']
#         phone = request.form['phone']
        
#         profile_photo = request.files['profile_photo']
        
#         if profile_photo:
#             profile_photo_filename = f"{user_id}_profile.jpg"
#             profile_photo_path = os.path.join(app.config['UPLOAD_FOLDER'], profile_photo_filename)
#             profile_photo.save(profile_photo_path)

#         employee_info = f"{employee_name},{user_id},{email},{phone},{profile_photo_filename}\n"
#         with open('employees.txt', 'a') as f:
#             f.write(employee_info)

#         return "✅ Registration Successful!"
#     return render_template('register.html')

# # -----> Upload Captured 50 Burst Images
# @app.route('/upload_captured_images', methods=['POST'])
# def upload_captured_images():
#     user_id = request.form.get('user_id')
#     dataset_path = os.path.join(app.config['DATASET_FOLDER'], user_id)
#     os.makedirs(dataset_path, exist_ok=True)

#     files = request.files.getlist('images')
#     for idx, file in enumerate(files):
#         filename = f"{user_id}_{idx}.jpg"
#         file.save(os.path.join(dataset_path, filename))

#     return "Captured images uploaded successfully!", 200

# if __name__ == '__main__':
#     app.run(debug=True)



# .........................code 3......................
# from flask import Flask, render_template, request, redirect, url_for
# import os

# app = Flask(__name__, static_folder='static', template_folder='templates')

# # Paths
# app.config['UPLOAD_FOLDER'] = 'uploads/profile_photos'
# app.config['DATASET_FOLDER'] = 'uploads/dataset'

# # Ensure folders exist
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
# os.makedirs(app.config['DATASET_FOLDER'], exist_ok=True)

# # -----> Home Route (Login Page First)
# @app.route('/')
# def home():
#     return render_template('login.html')

# # -----> New: Home page after login
# @app.route('/home')
# def homepage():
#     return render_template('home.html')

# # -----> Login Logic
# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form['username']
#     password = request.form['password']

#     # Example: basic check (you can connect DB later)
#     if username == "admin" and password == "admin123":
#         return redirect(url_for('register'))
#     else:
#         return "❌ Invalid credentials!"

# # -----> Registration Page
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         employee_name = request.form['employee_name']
#         user_id = request.form['user_id']
#         email = request.form['email']
#         phone = request.form['phone']
        
#         profile_photo = request.files['profile_photo']
        
#         if profile_photo:
#             profile_photo_filename = f"{user_id}_profile.jpg"
#             profile_photo_path = os.path.join(app.config['UPLOAD_FOLDER'], profile_photo_filename)
#             profile_photo.save(profile_photo_path)

#         employee_info = f"{employee_name},{user_id},{email},{phone},{profile_photo_filename}\n"
#         with open('employees.txt', 'a') as f:
#             f.write(employee_info)

#         return "✅ Registration Successful!"
#     return render_template('register.html')

# # -----> Upload Captured 50 Burst Images
# @app.route('/upload_captured_images', methods=['POST'])
# def upload_captured_images():
#     user_id = request.form.get('user_id')
#     dataset_path = os.path.join(app.config['DATASET_FOLDER'], user_id)
#     os.makedirs(dataset_path, exist_ok=True)

#     files = request.files.getlist('images')
#     for idx, file in enumerate(files):
#         filename = f"{user_id}_{idx}.jpg"
#         file.save(os.path.join(dataset_path, filename))

#     return "Captured images uploaded successfully!", 200

# if __name__ == '__main__':
#     app.run(debug=True)





# ............................code 4.................
# from flask import Flask, render_template, request, redirect, url_for, jsonify
# import os
# import datetime
# from werkzeug.utils import secure_filename

# app = Flask(__name__)

# # Path to save uploaded profile pictures and captured images
# UPLOAD_FOLDER_PROFILE = 'static/profile_pics'
# UPLOAD_FOLDER_DATASET = 'static/dataset'

# # Make sure folders exist
# os.makedirs(UPLOAD_FOLDER_PROFILE, exist_ok=True)
# os.makedirs(UPLOAD_FOLDER_DATASET, exist_ok=True)

# # Dummy database (replace later with real database if needed)
# employees = []
# attendance_records = []

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/home')
# def home():
#     return render_template('home.html')

# @app.route('/register')
# def register_employee():
#     return render_template('register.html')

# @app.route('/admin_r')
# def admin_register():
#     return render_template('admin_r.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         # Dummy login logic (you can connect with DB later)
#         username = request.form['username']
#         password = request.form['password']
#         if username == 'admin' and password == 'admin':
#             return redirect(url_for('home'))
#         else:
#             return "Invalid Credentials", 401
#     return render_template('login.html')

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

# @app.route('/employee')
# def employee_details():
#     return render_template('employee.html')

# # Save employee profile picture and basic details
# @app.route('/save_employee', methods=['POST'])
# def save_employee():
#     emp_id = request.form.get('emp_id')
#     name = request.form.get('name')
#     profile_pic = request.files.get('profile_pic')

#     if not emp_id or not name or not profile_pic:
#         return "Missing data", 400

#     # Save profile picture
#     filename = secure_filename(profile_pic.filename)
#     save_path = os.path.join(UPLOAD_FOLDER_PROFILE, filename)
#     profile_pic.save(save_path)

#     # Save employee details
#     employees.append({
#         'userid': emp_id,
#         'username': name,
#         'photo': url_for('static', filename=f'profile_pics/{filename}'),
#         'email': '',  # You can add more fields if needed
#         'phone': ''
#     })

#     return redirect(url_for('dashboard'))

# # Save each captured face image
# @app.route('/save_image', methods=['POST'])
# def save_image():
#     emp_id = request.form.get('emp_id')
#     image = request.files.get('image')

#     if not emp_id or not image:
#         return "Missing data", 400

#     timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
#     filename = f"{emp_id}_{timestamp}.jpg"
#     save_path = os.path.join(UPLOAD_FOLDER_DATASET, filename)
#     image.save(save_path)

#     return "Image Saved", 200

# # APIs for AngularJS app to get employees and their details
# @app.route('/api/employees')
# def api_employees():
#     return jsonify(employees)

# @app.route('/api/employee/<userid>')
# def api_employee(userid):
#     employee = next((e for e in employees if e['userid'] == userid), None)
#     if employee:
#         user_attendance = [record for record in attendance_records if record['userid'] == userid]
#         return jsonify({
#             'employee': employee,
#             'attendance': user_attendance
#         })
#     else:
#         return jsonify({'error': 'Employee not found'}), 404

# # Dummy route to simulate marking attendance (Optional future)
# @app.route('/mark_attendance', methods=['POST'])
# def mark_attendance():
#     userid = request.form.get('userid')
#     if userid:
#         attendance_records.append({
#             'userid': userid,
#             'date': datetime.datetime.now().strftime("%Y-%m-%d"),
#             'login': datetime.datetime.now().strftime("%H:%M:%S")
#         })
#         return "Attendance Marked", 200
#     else:
#         return "Missing userid", 400

# if __name__ == '__main__':
#     app.run(debug=True)

# .................. code 5..........................
# from flask import Flask, render_template, request, redirect, url_for, jsonify
# import os
# import datetime
# from werkzeug.utils import secure_filename

# app = Flask(__name__)
# # Connect to MySQL Database
# try:
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="test",
#         password="Test@1234",
#         database="attendance_db"
#     )
#     mycursor = mydb.cursor()
#     print("✅ Connected to MySQL Database!")
# except mysql.connector.Error as err:
#     print(f"❌ Error: {err}")


# UPLOAD_FOLDER_PROFILE = 'static/profile_pics'
# UPLOAD_FOLDER_DATASET = 'static/dataset'

# os.makedirs(UPLOAD_FOLDER_PROFILE, exist_ok=True)
# os.makedirs(UPLOAD_FOLDER_DATASET, exist_ok=True)

# employees = []
# attendance_records = []

# @app.route('/')
# def index():
#     return render_template('login.html')

# @app.route('/home')
# def home():
#     return render_template('home.html')

# @app.route('/register')
# def register():
#     return render_template('register.html')

# @app.route('/admin_r')
# def admin_r():
#     return render_template('admin_r.html')

# # @app.route('/dashboard')
# # def dashboard():
# #     return render_template('dashboard.html')

# @app.route('/dashboard')
# def dashboard():
#     user = "Admin"  # or fetch the user from your login session
#     return render_template('dashboard.html', user=user)


# @app.route('/employee')
# def employee():
#     return render_template('employee.html')

# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form.get('username')
#     password = request.form.get('password')
#     if username == "admin" and password == "admin":
#         return redirect(url_for('home'))
#     return "Invalid credentials", 401

# @app.route('/save_employee', methods=['POST'])
# def save_employee():
#     emp_id = request.form.get('emp_id')
#     name = request.form.get('name')
#     profile_pic = request.files.get('profile_pic')

#     if not emp_id or not name or not profile_pic:
#         return "Missing fields", 400

#     filename = secure_filename(profile_pic.filename)
#     profile_path = os.path.join(UPLOAD_FOLDER_PROFILE, filename)
#     profile_pic.save(profile_path)

#     employee_data = {
#         'userid': emp_id,
#         'username': name,
#         'photo': url_for('static', filename=f'profile_pics/{filename}'),
#         'email': '',
#         'phone': ''
#     }
#     employees.append(employee_data)

#     return redirect(url_for('dashboard'))

# @app.route('/save_image', methods=['POST'])
# def save_image():
#     emp_id = request.form.get('emp_id')
#     image = request.files.get('image')

#     if not emp_id or not image:
#         return "Missing data", 400

#     timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
#     filename = f"{emp_id}_{timestamp}.jpg"
#     save_path = os.path.join(UPLOAD_FOLDER_DATASET, filename)
#     image.save(save_path)

#     return "Image Saved", 200

# @app.route('/api/employees')
# def api_employees():
#     return jsonify(employees)

# @app.route('/api/employee/<userid>')
# def api_employee(userid):
#     employee = next((emp for emp in employees if emp['userid'] == userid), None)
#     if employee:
#         attendance = [att for att in attendance_records if att['userid'] == userid]
#         return jsonify({'employee': employee, 'attendance': attendance})
#     return jsonify({'error': 'Employee not found'}), 404

# if __name__ == '__main__':
#     app.run(debug=True)


# ................ code 6....................
# from flask import Flask, render_template, request, redirect, url_for, jsonify
# import os
# import datetime
# import mysql.connector
# from werkzeug.utils import secure_filename

# app = Flask(__name__)

# # Connect to MySQL Database
# try:
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="test",
#         password="Test@1234",
#         database="attendance_db"
#     )
#     mycursor = mydb.cursor()
#     print("✅ Connected to MySQL Database!")
# except mysql.connector.Error as err:
#     print(f"❌ Error: {err}")

# UPLOAD_FOLDER_PROFILE = 'static/profile_pics'
# UPLOAD_FOLDER_DATASET = 'static/dataset'

# os.makedirs(UPLOAD_FOLDER_PROFILE, exist_ok=True)
# os.makedirs(UPLOAD_FOLDER_DATASET, exist_ok=True)

# attendance_records = []

# @app.route('/')
# def index():
#     return render_template('login.html')

# @app.route('/home')
# def home():
#     return render_template('home.html')

# @app.route('/register')
# def register():
#     return render_template('register.html')

# @app.route('/admin_r')
# def admin_r():
#     return render_template('admin_r.html')

# @app.route('/dashboard')
# def dashboard():
#     user = "Admin"  # or fetch the user from your login session
#     return render_template('dashboard.html', user=user)

# @app.route('/employee')
# def employee():
#     return render_template('employee.html')

# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form.get('username')
#     password = request.form.get('password')
#     if username == "admin" and password == "admin":
#         return redirect(url_for('home'))
#     return "Invalid credentials", 401

# # ✅ Updated Save Employee - Now saving into MySQL database
# @app.route('/save_employee', methods=['POST'])
# def save_employee():
#     emp_id = request.form.get('emp_id')
#     name = request.form.get('name')
#     profile_pic = request.files.get('profile_pic')

#     if not emp_id or not name or not profile_pic:
#         return "Missing fields", 400

#     filename = secure_filename(profile_pic.filename)
#     profile_path = os.path.join(UPLOAD_FOLDER_PROFILE, filename)
#     profile_pic.save(profile_path)

#     # Save employee into MySQL database
#     try:
#         conn = mysql.connector.connect(
#             host="localhost",
#             user="test",
#             password="Test@1234",
#             database="attendance_db"
#         )
#         cursor = conn.cursor()

#         # Assuming you have a table called `employees`
#         insert_query = """
#             INSERT INTO employees (emp_id, name, photo)
#             VALUES (%s, %s, %s)
#         """
#         photo_url = f'static/profile_pics/{filename}'
#         cursor.execute(insert_query, (emp_id, name, photo_url))

#         conn.commit()
#         cursor.close()
#         conn.close()

#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         return "Database error", 500

#     return redirect(url_for('dashboard'))

# @app.route('/save_image', methods=['POST'])
# def save_image():
#     emp_id = request.form.get('emp_id')
#     image = request.files.get('image')

#     if not emp_id or not image:
#         return "Missing data", 400

#     timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
#     filename = f"{emp_id}_{timestamp}.jpg"
#     save_path = os.path.join(UPLOAD_FOLDER_DATASET, filename)
#     image.save(save_path)

#     return "Image Saved", 200

# @app.route('/api/employees')
# def api_employees():
#     try:
#         conn = mysql.connector.connect(
#             host="localhost",
#             user="test",
#             password="Test@1234",
#             database="attendance_db"
#         )
#         cursor = conn.cursor(dictionary=True)
#         cursor.execute("SELECT emp_id AS userid, name AS username, photo FROM employees")
#         employees = cursor.fetchall()
#         cursor.close()
#         conn.close()
#         return jsonify(employees)
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         return jsonify([])

# @app.route('/api/employee/<userid>')
# def api_employee(userid):
#     try:
#         conn = mysql.connector.connect(
#             host="localhost",
#             user="test",
#             password="Test@1234",
#             database="attendance_db"
#         )
#         cursor = conn.cursor(dictionary=True)
#         cursor.execute("SELECT emp_id AS userid, name AS username, photo FROM employees WHERE emp_id = %s", (userid,))
#         employee = cursor.fetchone()

#         cursor.close()
#         conn.close()

#         if employee:
#             attendance = [att for att in attendance_records if att['userid'] == userid]
#             return jsonify({'employee': employee, 'attendance': attendance})
#         else:
#             return jsonify({'error': 'Employee not found'}), 404

#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         return jsonify({'error': 'Database error'}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, request, jsonify
# import os
# import mysql.connector

# app = Flask(__name__)

# # Configure your MySQL connection
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="your_password",
#     database="your_database"
# )
# cursor = db.cursor()

# UPLOAD_FOLDER = 'static/uploads/'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route('/save_employee', methods=['POST'])
# def save_employee():
#     emp_id = request.form['emp_id']
#     name = request.form['name']
#     email = request.form['email']  # ✅ New
#     phone = request.form['phone']  # ✅ New

#     if 'photo' not in request.files:
#         return jsonify({'error': 'No photo uploaded'}), 400

#     photo = request.files['photo']
#     photo_filename = emp_id + '_' + photo.filename
#     photo.save(os.path.join(UPLOAD_FOLDER, photo_filename))

#     # Save details to MySQL
#     insert_query = """
#     INSERT INTO employees (emp_id, name, email, phone, photo)
#     VALUES (%s, %s, %s, %s, %s)
#     """
#     values = (emp_id, name, email, phone, photo_filename)
#     cursor.execute(insert_query, values)
#     db.commit()

#     return jsonify({'message': 'Employee saved successfully'})





# ..................... code 7.............
# from flask import Flask, render_template, request, redirect, url_for, jsonify
# import os
# import datetime
# import mysql.connector
# from werkzeug.utils import secure_filename

# app = Flask(__name__)

# # Upload folders
# UPLOAD_FOLDER_PROFILE = 'static/profile_pics'
# UPLOAD_FOLDER_DATASET = 'static/dataset'
# UPLOAD_FOLDER_UPLOADS = 'static/uploads'

# os.makedirs(UPLOAD_FOLDER_PROFILE, exist_ok=True)
# os.makedirs(UPLOAD_FOLDER_DATASET, exist_ok=True)
# os.makedirs(UPLOAD_FOLDER_UPLOADS, exist_ok=True)

# # MySQL configuration
# def get_db_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="test",  # Change if needed
#         password="Test@1234",  # Change if needed
#         database="attendance_db"
#     )

# attendance_records = []

# # --- Routes ---
# @app.route('/')
# def index():
#     return render_template('login.html')

# @app.route('/home')
# def home():
#     return render_template('home.html')

# @app.route('/register')
# def register():
#     return render_template('register.html')

# @app.route('/admin_r')
# def admin_r():
#     return render_template('admin_r.html')

# @app.route('/dashboard')
# def dashboard():
#     user = "Admin"
#     return render_template('dashboard.html', user=user)

# @app.route('/employee')
# def employee():
#     return render_template('employee.html')

# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form.get('username')
#     password = request.form.get('password')
#     if username == "admin" and password == "admin":
#         return redirect(url_for('home'))
#     return "Invalid credentials", 401

# # Save employee with email and phone
# @app.route('/save_employee', methods=['POST'])
# def save_employee():
#     emp_id = request.form.get('emp_id')
#     name = request.form.get('name')
#     email = request.form.get('email')
#     phone = request.form.get('phone')
#     photo = request.files.get('photo')

#     if not emp_id or not name or not email or not phone or not photo:
#         return jsonify({'error': 'Missing fields'}), 400

#     filename = secure_filename(emp_id + '_' + photo.filename)
#     photo_path = os.path.join(UPLOAD_FOLDER_UPLOADS, filename)
#     photo.save(photo_path)

#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         insert_query = """
#             INSERT INTO employees (emp_id, name, email, phone, photo)
#             VALUES (%s, %s, %s, %s, %s)
#         """
#         cursor.execute(insert_query, (emp_id, name, email, phone, filename))
#         conn.commit()
#         cursor.close()
#         conn.close()
#         return redirect(url_for('dashboard'))
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         return jsonify({'error': 'Database error'}), 500

# # Save employee dataset image
# @app.route('/save_image', methods=['POST'])
# def save_image():
#     emp_id = request.form.get('emp_id')
#     image = request.files.get('image')

#     if not emp_id or not image:
#         return "Missing data", 400

#     timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
#     filename = f"{emp_id}_{timestamp}.jpg"
#     save_path = os.path.join(UPLOAD_FOLDER_DATASET, filename)
#     image.save(save_path)

#     return "Image Saved", 200

# # API to fetch all employees
# @app.route('/api/employees')
# def api_employees():
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor(dictionary=True)
#         cursor.execute("SELECT emp_id AS userid, name AS username, email, phone, photo FROM employees")
#         employees = cursor.fetchall()
#         cursor.close()
#         conn.close()
#         return jsonify(employees)
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         return jsonify([])

# # API to fetch employee by ID
# @app.route('/api/employee/<userid>')
# def api_employee(userid):
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor(dictionary=True)
#         cursor.execute("SELECT emp_id AS userid, name AS username, email, phone, photo FROM employees WHERE emp_id = %s", (userid,))
#         employee = cursor.fetchone()
#         cursor.close()
#         conn.close()

#         if employee:
#             attendance = [att for att in attendance_records if att['userid'] == userid]
#             return jsonify({'employee': employee, 'attendance': attendance})
#         else:
#             return jsonify({'error': 'Employee not found'}), 404

#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         return jsonify({'error': 'Database error'}), 500

# if __name__ == '__main__':
#     app.run(debug=True)


# ...................code 8................
# from flask import Flask, render_template, request, redirect, url_for, jsonify
# import os
# import datetime
# import mysql.connector
# from werkzeug.utils import secure_filename

# app = Flask(__name__)

# # MySQL database config
# DB_CONFIG = {
#     "host": "localhost",
#     "user": "test",  # your MySQL username
#     "password": "Test@1234",  # your MySQL password
#     "database": "attendance_db"  # your database name
# }

# # Upload folders
# UPLOAD_FOLDER_PROFILE = 'static/profile_pics'
# UPLOAD_FOLDER_DATASET = 'static/dataset'
# UPLOAD_FOLDER_UPLOADS = 'static/uploads'

# # Make sure folders exist
# os.makedirs(UPLOAD_FOLDER_PROFILE, exist_ok=True)
# os.makedirs(UPLOAD_FOLDER_DATASET, exist_ok=True)
# os.makedirs(UPLOAD_FOLDER_UPLOADS, exist_ok=True)

# attendance_records = []

# # Function to get DB connection
# def get_db_connection():
#     return mysql.connector.connect(**DB_CONFIG)

# @app.route('/')
# def index():
#     return render_template('login.html')

# @app.route('/home')
# def home():
#     return render_template('home.html')

# @app.route('/register')
# def register():
#     return render_template('register.html')

# @app.route('/admin_r')
# def admin_r():
#     return render_template('admin_r.html')

# @app.route('/dashboard')
# def dashboard():
#     user = "Admin"
#     return render_template('dashboard.html', user=user)

# @app.route('/employee')
# def employee():
#     return render_template('employee.html')

# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form.get('username')
#     password = request.form.get('password')
#     if username == "admin" and password == "admin":
#         return redirect(url_for('home'))
#     return "Invalid credentials", 401

# # ✅ Save new employee
# # @app.route('/save_employee', methods=['POST'])
# # def save_employee():
# #     emp_id = request.form.get('emp_id')
# #     name = request.form.get('name')
# #     email = request.form.get('email')
# #     phone = request.form.get('phone')
# #     photo = request.files.get('photo')

# #     if not emp_id or not name or not email or not phone or not photo:
# #         return jsonify({'error': 'Missing fields'}), 400

# #     photo_filename = secure_filename(emp_id + '_' + photo.filename)
# #     photo_path = os.path.join(UPLOAD_FOLDER_UPLOADS, photo_filename)
# #     photo.save(photo_path)

# #     try:
# #         conn = get_db_connection()
# #         cursor = conn.cursor()

# #         insert_query = """
# #             INSERT INTO employees (emp_id, name, email, phone, photo)
# #             VALUES (%s, %s, %s, %s, %s)
# #         """
# #         cursor.execute(insert_query, (emp_id, name, email, phone, photo_filename))
# #         conn.commit()

# #         cursor.close()
# #         conn.close()

# #     except mysql.connector.Error as err:
# #         print(f"Database Error: {err}")
# #         return jsonify({'error': 'Database error'}), 500

# #     return jsonify({'message': 'Employee saved successfully'}), 200

# from flask import Flask, request, jsonify
# from werkzeug.utils import secure_filename
# import os
# import mysql.connector

# app = Flask(__name__)
# UPLOAD_FOLDER_UPLOADS = 'uploads'  # Make sure this folder exists!

# @app.route('/save_employee', methods=['POST'])
# def save_employee():
#     emp_id = request.form.get('emp_id')
#     name = request.form.get('name')
#     email = request.form.get('email')
#     phone = request.form.get('phone')
#     photo = request.files.get('photo')

#     if not emp_id or not name or not email or not phone or not photo:
#         return jsonify({'error': 'Missing fields'}), 400

#     # Save the uploaded photo
#     photo_filename = secure_filename(emp_id + '_' + photo.filename)
#     photo_path = os.path.join(UPLOAD_FOLDER_UPLOADS, photo_filename)
#     photo.save(photo_path)

#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor()

#         insert_query = """
#             INSERT INTO employees (emp_id, name, email, phone, photo)
#             VALUES (%s, %s, %s, %s, %s)
#         """
#         cursor.execute(insert_query, (emp_id, name, email, phone, photo_filename))
#         conn.commit()

#     except mysql.connector.Error as err:
#         print(f"Database Error: {err}")
#         return jsonify({'error': 'Database error'}), 500

#     finally:
#         cursor.close()
#         conn.close()

#     return jsonify({'message': 'Employee saved successfully'}), 200


# # ✅ Save captured image to dataset
# @app.route('/save_image', methods=['POST'])
# def save_image():
#     emp_id = request.form.get('emp_id')
#     image = request.files.get('image')

#     if not emp_id or not image:
#         return "Missing data", 400

#     timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
#     filename = f"{emp_id}_{timestamp}.jpg"
#     save_path = os.path.join(UPLOAD_FOLDER_DATASET, filename)
#     image.save(save_path)

#     return "Image Saved", 200

# # ✅ API to get all employees
# @app.route('/api/employees')
# def api_employees():
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor(dictionary=True)
#         cursor.execute("SELECT emp_id AS userid, name AS username, photo FROM employees")
#         employees = cursor.fetchall()
#         cursor.close()
#         conn.close()
#         return jsonify(employees)
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         return jsonify([])

# # ✅ API to get one employee + attendance
# @app.route('/api/employee/<userid>')
# def api_employee(userid):
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor(dictionary=True)
#         cursor.execute("SELECT emp_id AS userid, name AS username, photo FROM employees WHERE emp_id = %s", (userid,))
#         employee = cursor.fetchone()
#         cursor.close()
#         conn.close()

#         if employee:
#             attendance = [att for att in attendance_records if att['userid'] == userid]
#             return jsonify({'employee': employee, 'attendance': attendance})
#         else:
#             return jsonify({'error': 'Employee not found'}), 404
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         return jsonify({'error': 'Database error'}), 500

# if __name__ == '__main__':
#     app.run(debug=True)








# ............... code 9......................
from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os
import datetime
import mysql.connector

app = Flask(__name__)

# MySQL database config
DB_CONFIG = {
    "host": "localhost",
    "user": "test",  # your MySQL username
    "password": "Test@1234",  # your MySQL password
    "database": "attendance_db"  # your database name
}

# # Upload folders
# UPLOAD_FOLDER_PROFILE = 'static/profile_pics'
# UPLOAD_FOLDER_DATASET = 'static/dataset'
# UPLOAD_FOLDER_UPLOADS = 'static/uploads'

# # Ensure folders exist
# os.makedirs(UPLOAD_FOLDER_PROFILE, exist_ok=True)
# os.makedirs(UPLOAD_FOLDER_DATASET, exist_ok=True)
# os.makedirs(UPLOAD_FOLDER_UPLOADS, exist_ok=True)

attendance_records = []

# Function to get DB connection
def get_db_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Database connection failed: {err}")
        raise

# Routes
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/admin_r')
def admin_r():
    return render_template('admin_r.html')

@app.route('/dashboard')
def dashboard():
    user = "Admin"
    return render_template('dashboard.html', user=user)

@app.route('/employee')
def employee():
    return render_template('employee.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == "admin" and password == "admin":
        return redirect(url_for('home'))
    return "Invalid credentials", 401

# ✅ Save new employee

@app.route('/save_employee', methods=['POST'])
def save_employee():
    emp_id = request.form.get('emp_id')
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    photo = request.files.get('photo')

    if not emp_id or not name or not email or not phone or not photo:
        return jsonify({'error': 'Missing fields'}), 400

    # # Save the uploaded photo
    # photo_filename = secure_filename(emp_id + '_' + photo.filename)
    # photo_path = os.path.join(UPLOAD_FOLDER_UPLOADS, photo_filename)
    # photo.save(photo_path)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        insert_query = """
            INSERT INTO employees (emp_id, name, email, phone, photo)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (emp_id, name, email, phone, photo))
        conn.commit()

        return jsonify({'message': 'Employee saved successfully'}), 200

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return jsonify({'error': 'Database error'}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# # ✅ Save captured image to dataset
# @app.route('/save_image', methods=['POST'])
# def save_image():
#     emp_id = request.form.get('emp_id')
#     image = request.files.get('image')

#     if not emp_id or not image:
#         return "Missing data", 400

#     timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
#     filename = f"{emp_id}_{timestamp}.jpg"
#     save_path = os.path.join(UPLOAD_FOLDER_DATASET, filename)
#     image.save(save_path)

#     return "Image Saved", 200

# ✅ API to get all employees
@app.route('/api/employees')
def api_employees():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT emp_id AS userid, name AS username, photo FROM employees")
        employees = cursor.fetchall()
        return jsonify(employees)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify([])
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# ✅ API to get one employee + attendance
@app.route('/api/employee/<userid>')
def api_employee(userid):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT emp_id AS userid, name AS username, photo FROM employees WHERE emp_id = %s", (userid,))
        employee = cursor.fetchone()

        if employee:
            attendance = [att for att in attendance_records if att['userid'] == userid]
            return jsonify({'employee': employee, 'attendance': attendance})
        else:
            return jsonify({'error': 'Employee not found'}), 404

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({'error': 'Database error'}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)