## 📘 Numerical Analysis
--- 
**Task Code: NAML-01**: [Implementation](NMAL-01.py)


#### 📌 Traditional Approach
- Manually pick an interval \([a, b]\)
- Success depends on lucky guessing

#### 💡 Improved Approach
- Automate interval detection:
  - Loop over \([x, x + \delta]\)
  - Check if \( f(x) \cdot f(x + \delta) < 0 \)
  - If yes, use \([x, x + \delta]\) as the root interval

### ⚙️ Sample Test

- Enter start of the interval: 0
- Enter end of the interval: 5
- Enter the step size for scanning: 0.1
- Enter the error tolerance: 0.001
- Traditional bisection root: 1.5216064453125, iterations: 12
- Improved bisection root: 1.5210937500000004, iterations: 6

---
