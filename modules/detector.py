import cv2


class CarsDetection:

    def __init__(self):
        net = cv2.dnn.readNet("dnn_model/yolov4.weights", "dnn_model/yolov4.cfg")
        self.model = cv2.dnn_DetectionModel(net)
        self.model.setInputParams(size=(832, 832), scale=1 / 255)
        self.classes_allowed = [2, 3, 5, 6, 7]

    def detect_car(self, img):
        vehicles_boxes = []
        class_ids, scores, boxes = self.model.detect(img, nmsThreshold=0.4)
        for class_id, score, box in zip(class_ids, scores, boxes):
            if score < 0.5:
                continue
            if class_id in self.classes_allowed:
                vehicles_boxes.append(box)
        for box in vehicles_boxes:
            x, y, w, h = box
            cv2.rectangle(img, (x, y), (x + w, y + h), (30, 30, 255), 1)
        return img, len(vehicles_boxes)
