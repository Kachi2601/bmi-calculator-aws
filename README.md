# bmi-calculator-aws

# 🧮 Cloud-Hosted BMI Calculator App

This project simulates a real-world cloud and DevOps workflow by building and deploying a BMI calculator application with full infrastructure automation and CI/CD pipelines (eventually).

The app allows users to input basic personal information (name, age, gender, height, weight), calculates their BMI, and stores the data in a database.

---

## 🔧 Current Tech Stack (Phase 1)

- **Python** & **Flask** – to handle routing, logic, and form submission
- **HTML/CSS** – for the front-end user interface
- **Docker** – to containerize the full application (planned)
- **AWS EC2** – to host and serve the Dockerized app
- **Terraform** – to provision cloud infrastructure
- **GitHub Actions** – for automating deployments (manual for now)

---

## 🚧 Challenges & In-Progress Considerations

- 🔄 **Database Integration**: Still deciding between local databases or AWS RDS. Connecting Flask securely to RDS (if chosen) is something I’ll address in a later phase.
- 📦 **Docker Compatibility**: Verifying that the Flask + HTML/CSS front end can be properly containerized and deployed in a stable Docker image.
- 🚀 **ECR & CloudWatch**: These services are planned for later stages as I build on the project. For now, deployment and logging are kept simple and local where possible.

---

## 📌 Project Goal

To simulate a production-ready cloud deployment pipeline by combining real DevOps practices with a functioning web application. This isn’t just about building a BMI calculator — it’s about proving I can structure, deploy, and scale a cloud-native app.

---

## ✅ Future Plans

- Add proper database integration (possibly AWS RDS)
- Integrate CloudWatch logging and monitoring
- Automate CI/CD using GitHub Actions to build and push to AWS ECR
- Polish the UI and collect feedback

---

## 🤝 Contributions

This project is part of my journey to deepen my DevOps and Cloud Engineering skills. Feedback, suggestions, or similar project stories are welcome!

---

## 📌 Status

🚧 **In development** — Follow along as I document each phase.
