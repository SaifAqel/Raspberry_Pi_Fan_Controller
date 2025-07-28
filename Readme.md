# 🌀 Raspberry Pi Fan Controller

A Python-based fan controller for Raspberry Pi that automatically adjusts the speed of a connected 5V PWM fan based on CPU temperature.

✅ **Two Operating Modes**:
- 🔄 **Smooth**: Fan speed changes *linearly* with temperature.
- 📶 **Stepped**: Fan speed increases in *defined temperature bands*.

---

## 🛠️ Requirements

- Raspberry Pi (any model with GPIO support)
- 5V PWM-compatible fan connected to **GPIO14 (BCM)**
- Raspberry Pi OS (vcgencmd must be available)
- Python 3
- `RPi.GPIO` Python library

To install the required library:
```bash
sudo apt install python3-rpi.gpio
```

---

## 🚀 Usage

1. Run the script:
```bash
python3 main.py
```

2. When prompted, choose a mode:
```
Select mode [smooth / stepped]: smooth
```

---

## 🧠 How It Works

- **Smooth mode** uses a linear function to map the CPU temperature (e.g., 25°C–80°C) to fan duty cycle (e.g., 0%–100%).
- **Stepped mode** sets the fan to fixed speeds based on temperature brackets (e.g., 25–32°C → 15%, 50–60°C → 70%, etc.).

---

## ⚠️ Wiring Diagram

```
Fan PWM (usually yellow wire) → GPIO14 (BCM)
Fan Power (red)              → 5V
Fan Ground (black)           → GND
```

> Make sure your fan supports **PWM control** (not just 2-pin or voltage control).

---

## 👨‍💻 Author

Modified and extended by **Saif Aqel**
Originally created by [Michael Klements](https://www.the-diy-life.com/connecting-a-pwm-fan-to-a-raspberry-pi/).

---

## 📄 License

This project is open-source under the MIT License.

---

## 🧪 Future Improvements

- OLED display integration
- Logging & graphing temperature vs speed
- Web dashboard for control and monitoring
