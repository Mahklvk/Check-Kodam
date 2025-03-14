from flask import Flask, render_template, Response, request, redirect, url_for
import cv2
import mediapipe as mp
import random
import os
import uuid
from threading import Thread

app = Flask(__name__)

# Inisialisasi MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.3)

# Folder untuk menyimpan foto
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Inisialisasi kamera di thread terpisah
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def generate_random_text():
    words = [
        "Karbu", "Beat", "Jagung", "Bakwan", "Singa", "Polisi", "Bayar", "NVIDIA", "INTEL", "Pentium", "Gucci", "Vario",
        "Orang", "Utan", "Mio", "Solder", "Covid", ""
        
        ]
    return ' '.join(random.sample(words, 2))

def gen_frames():
    frame_count = 0
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            frame_count += 1
            if frame_count % 5 == 0:  # Deteksi wajah setiap 5 frame
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = face_detection.process(rgb_frame)
                if results.detections:
                    for detection in results.detections:
                        bboxC = detection.location_data.relative_bounding_box
                        ih, iw, _ = frame.shape
                        x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                                     int(bboxC.width * iw), int(bboxC.height * ih)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        text = generate_random_text()
                        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture', methods=['POST'])
def capture():
    success, frame = camera.read()
    if not success:
        return "Gagal mengambil foto", 400

    # Kompres gambar
    _, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
    frame = cv2.imdecode(buffer, cv2.IMREAD_COLOR)

    # Simpan gambar
    random_filename = str(uuid.uuid4()) + '.jpg'
    filepath = os.path.join(UPLOAD_FOLDER, random_filename)
    cv2.imwrite(filepath, frame)

    # Generate teks random
    random_text = generate_random_text()

    return redirect(url_for('result', text=random_text, filename=random_filename))

@app.route('/result')
def result():
    text = request.args.get('text', 'Tidak ada teks')
    filename = request.args.get('filename', '')
    return render_template('result.html', text=text, filename=filename)

if __name__ == '__main__':
    app.run(debug=True)