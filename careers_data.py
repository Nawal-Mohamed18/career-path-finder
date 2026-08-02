"""Career catalog, roadmaps, and quiz scoring for Career Path Finder."""

CAREERS = {
    "fullstack": {
        "title": "Full-Stack Web Development",
        "tagline": "Build complete web apps — frontend, backend, and the glue between them.",
        "skills": ["HTML/CSS", "JavaScript", "Backend framework", "Databases", "APIs", "Git"],
        "path": [
            "Learn HTML, CSS, and modern JavaScript firmly.",
            "Build interactive UIs (React, Vue, or similar).",
            "Learn a backend (Flask/Django, Node, or equivalent) and REST APIs.",
            "Use a database (SQL first, then optional NoSQL).",
            "Ship 2–3 full projects: auth, CRUD, and deployment.",
            "Learn Git, testing basics, and hosting (e.g. Render, Vercel, or a VPS).",
            "Apply for junior full-stack / web developer roles with a live portfolio.",
        ],
    },
    "mobile": {
        "title": "Mobile Application Development",
        "tagline": "Design and ship apps people use on phones every day.",
        "skills": ["Mobile UI", "Kotlin/Swift or Flutter/React Native", "APIs", "App store release", "Debugging"],
        "path": [
            "Choose a track: native (Kotlin/Swift) or cross-platform (Flutter/React Native).",
            "Learn mobile UI patterns, navigation, and device basics.",
            "Connect apps to APIs and local storage.",
            "Build 2–3 apps (list/detail, forms, offline-friendly feature).",
            "Practice debugging, performance, and accessibility on real devices.",
            "Publish at least one app (or TestFlight / internal track).",
            "Apply for junior mobile developer roles with store links or demos.",
        ],
    },
    "networking": {
        "title": "Networking",
        "tagline": "Design, connect, and keep networks reliable and secure.",
        "skills": ["TCP/IP", "Routing & switching", "LAN/WAN", "Troubleshooting", "Network security basics"],
        "path": [
            "Learn networking fundamentals: OSI/TCP-IP, IP addressing, subnets.",
            "Practice with Packet Tracer, GNS3, or real lab gear.",
            "Study routing, switching, VLANs, and wireless basics.",
            "Learn troubleshooting methodically (cables → config → services).",
            "Add network security basics: firewalls, ACLs, secure remote access.",
            "Earn a foundational cert if useful (e.g. CompTIA Network+ or CCNA path).",
            "Aim for junior network technician / NOC / support roles.",
        ],
    },
    "cybersecurity": {
        "title": "Cybersecurity",
        "tagline": "Protect systems, data, and people from threats.",
        "skills": ["Security fundamentals", "Networking", "OS hardening", "Threat awareness", "Scripting"],
        "path": [
            "Learn security basics: CIA triad, threats, common attack types.",
            "Strengthen networking and OS skills (Linux + Windows).",
            "Practice in beginner labs (TryHackMe / similar defensive paths).",
            "Learn scripting (Python/Bash) for automation and log analysis.",
            "Study defensive tools: SIEM basics, firewalls, identity controls.",
            "Document lab write-ups and one small hardening project.",
            "Apply for SOC analyst / junior security roles (Security+ optional).",
        ],
    },
    "cloud": {
        "title": "Cloud Computing",
        "tagline": "Build and run systems on cloud platforms at scale.",
        "skills": ["Cloud core services", "Networking in cloud", "IAM", "Containers basics", "Cost & reliability"],
        "path": [
            "Pick a primary cloud (AWS, Azure, or GCP) and learn its core services.",
            "Practice compute, storage, networking, and identity (IAM).",
            "Deploy a simple app end-to-end in the cloud.",
            "Learn containers and basic orchestration concepts (Docker first).",
            "Study reliability: monitoring, backups, high availability basics.",
            "Earn a foundational cloud cert if it helps your job market.",
            "Apply for cloud support / junior cloud engineer roles with demos.",
        ],
    },
    "sysadmin": {
        "title": "System Administration",
        "tagline": "Keep servers, users, and services running smoothly.",
        "skills": ["Linux/Windows admin", "Scripting", "Users & permissions", "Monitoring", "Backup & recovery"],
        "path": [
            "Get strong on one OS deeply (Linux recommended) plus Windows basics.",
            "Learn users, permissions, services, packaging, and file systems.",
            "Automate with Bash/PowerShell and simple Python scripts.",
            "Practice networking services: DNS, DHCP, SSH, web servers.",
            "Learn monitoring, logs, backups, and recovery drills.",
            "Build a home lab: multiple VMs, documented runbooks.",
            "Apply for junior sysadmin / IT operations roles.",
        ],
    },
    "data_science_ml": {
        "title": "Data Science & Machine Learning",
        "tagline": "Turn data into models, insights, and predictions.",
        "skills": ["Python", "Statistics", "SQL", "ML libraries", "Visualization", "Experimentation"],
        "path": [
            "Learn Python for data work (pandas, numpy) and core statistics.",
            "Master SQL and exploratory analysis on real datasets.",
            "Build classical ML projects with scikit-learn and clear metrics.",
            "Practice feature work, validation, and honest evaluation.",
            "Create visualizations and short write-ups of your findings.",
            "Ship 3 portfolio projects with notebooks + plain-language conclusions.",
            "Apply for data science / ML junior roles or analytics-heavy paths.",
        ],
    },
    "ai": {
        "title": "Artificial Intelligence (AI)",
        "tagline": "Build intelligent systems — from models to usable products.",
        "skills": ["Python", "ML/DL fundamentals", "Neural nets", "APIs", "Evaluation", "Responsible AI basics"],
        "path": [
            "Build a strong Python + math foundation (linear algebra, probability).",
            "Learn ML fundamentals before jumping to deep learning.",
            "Study neural networks and one framework (PyTorch preferred).",
            "Build demos: vision, NLP, or generative AI with clear evaluation.",
            "Learn how to wrap models in APIs and simple UIs.",
            "Study limits, bias, and safe use — not only model accuracy.",
            "Apply for AI/ML engineer roles with end-to-end project proof.",
        ],
    },
    "iot": {
        "title": "Internet of Things (IoT)",
        "tagline": "Connect sensors, devices, and software into living systems.",
        "skills": ["Electronics basics", "Microcontrollers", "Networking", "Embedded programming", "Cloud/data basics"],
        "path": [
            "Learn electronics basics: circuits, sensors, actuators safely.",
            "Program microcontrollers (Arduino, ESP32, or Raspberry Pi).",
            "Connect devices over Wi-Fi/Bluetooth and send telemetry.",
            "Build a full loop: sense → process → act → dashboard.",
            "Learn IoT security basics and power/reliability constraints.",
            "Document 2–3 hardware+software projects with photos and code.",
            "Aim for IoT / embedded junior roles or related maker-to-job paths.",
        ],
    },
    "multimedia": {
        "title": "Multimedia",
        "tagline": "Create visual, audio, and interactive media experiences.",
        "skills": ["Design fundamentals", "Video/audio tools", "Motion/graphics", "Storytelling", "Export & delivery"],
        "path": [
            "Learn design fundamentals: composition, color, typography, hierarchy.",
            "Pick a primary craft: video, motion graphics, audio, or interactive media.",
            "Practice daily with one main tool stack (e.g. Premiere/After Effects/DaVinci, or Blender).",
            "Build a showreel of 4–6 short pieces with clear intent.",
            "Learn file formats, compression, and delivery for web/social/broadcast.",
            "Collaborate on one real client or campus/community project.",
            "Apply for junior multimedia / content / motion roles with a tight portfolio.",
        ],
    },
    "other": {
        "title": "Other",
        "tagline": "Your path is custom — clarify the destination, then build proof.",
        "skills": ["Clear goal definition", "Foundational learning", "Portfolio proof", "Networking", "Iteration"],
        "path": [
            "Write one sentence: the role or craft you want in 12–24 months.",
            "List the 5 skills that role actually requires (from real job posts).",
            "Choose one beginner project that forces those skills.",
            "Learn in public: notes, GitHub, or a simple portfolio page.",
            "Get feedback from one person already doing that work.",
            "Ship proof every week for 8 weeks (small, finished pieces).",
            "Apply, freelance, or intern using that proof — not only certificates.",
        ],
    },
}

# Quiz does not recommend "Other"; that path is chosen manually.
QUIZ_CAREERS = [key for key in CAREERS if key != "other"]

QUESTIONS = [
    {
        "id": "interest",
        "text": "What excites you most day to day?",
        "options": [
            {
                "label": "Building websites and web apps end to end",
                "scores": {"fullstack": 3, "mobile": 1},
            },
            {
                "label": "Making apps for phones and tablets",
                "scores": {"mobile": 3, "fullstack": 1},
            },
            {
                "label": "Connecting machines and keeping networks healthy",
                "scores": {"networking": 3, "sysadmin": 1, "cybersecurity": 1},
            },
            {
                "label": "Defending systems and hunting risks",
                "scores": {"cybersecurity": 3, "networking": 1},
            },
            {
                "label": "Running systems in the cloud",
                "scores": {"cloud": 3, "sysadmin": 1, "fullstack": 1},
            },
            {
                "label": "Keeping servers and services running",
                "scores": {"sysadmin": 3, "cloud": 1, "networking": 1},
            },
            {
                "label": "Finding patterns in data and training models",
                "scores": {"data_science_ml": 3, "ai": 2},
            },
            {
                "label": "Building intelligent AI systems and products",
                "scores": {"ai": 3, "data_science_ml": 2},
            },
            {
                "label": "Connecting sensors and physical devices",
                "scores": {"iot": 3, "networking": 1},
            },
            {
                "label": "Creating video, graphics, sound, or interactive media",
                "scores": {"multimedia": 3},
            },
        ],
    },
    {
        "id": "work_style",
        "text": "How do you like to work?",
        "options": [
            {
                "label": "Shipping product features users can click",
                "scores": {"fullstack": 3, "mobile": 2},
            },
            {
                "label": "Hands-on labs, configs, and infrastructure",
                "scores": {"networking": 2, "sysadmin": 3, "cloud": 2, "cybersecurity": 1},
            },
            {
                "label": "Investigation, hardening, and careful defense",
                "scores": {"cybersecurity": 3, "networking": 1},
            },
            {
                "label": "Experiments, notebooks, and measurable results",
                "scores": {"data_science_ml": 3, "ai": 2},
            },
            {
                "label": "Hardware + software prototypes in the physical world",
                "scores": {"iot": 3},
            },
            {
                "label": "Creative production and visual storytelling",
                "scores": {"multimedia": 3},
            },
        ],
    },
    {
        "id": "strength",
        "text": "Which strength feels most natural?",
        "options": [
            {
                "label": "Coding user-facing apps and APIs",
                "scores": {"fullstack": 3, "mobile": 2, "cloud": 1},
            },
            {
                "label": "Mobile UI and device-centered thinking",
                "scores": {"mobile": 3, "multimedia": 1},
            },
            {
                "label": "Protocols, packets, and connectivity",
                "scores": {"networking": 3, "cybersecurity": 1, "iot": 1},
            },
            {
                "label": "Risk awareness and security mindset",
                "scores": {"cybersecurity": 3, "networking": 1, "sysadmin": 1},
            },
            {
                "label": "Cloud services, automation, and scalable setup",
                "scores": {"cloud": 3, "sysadmin": 2, "fullstack": 1},
            },
            {
                "label": "Systems, scripts, and operational reliability",
                "scores": {"sysadmin": 3, "cloud": 1, "networking": 1},
            },
            {
                "label": "Math, stats, and analytical problem solving",
                "scores": {"data_science_ml": 3, "ai": 2},
            },
            {
                "label": "Deep learning / intelligent system design",
                "scores": {"ai": 3, "data_science_ml": 2},
            },
            {
                "label": "Electronics, sensors, and embedded tinkering",
                "scores": {"iot": 3},
            },
            {
                "label": "Visual / audio craft and creative direction",
                "scores": {"multimedia": 3},
            },
        ],
    },
    {
        "id": "goal",
        "text": "What outcome do you want in 2–3 years?",
        "options": [
            {
                "label": "Work as a full-stack / web developer",
                "scores": {"fullstack": 3},
            },
            {
                "label": "Ship mobile apps professionally",
                "scores": {"mobile": 3},
            },
            {
                "label": "Build or support enterprise networks",
                "scores": {"networking": 3},
            },
            {
                "label": "Protect organizations from cyber threats",
                "scores": {"cybersecurity": 3},
            },
            {
                "label": "Design and run cloud infrastructure",
                "scores": {"cloud": 3},
            },
            {
                "label": "Administer systems and keep ops stable",
                "scores": {"sysadmin": 3},
            },
            {
                "label": "Work in data science or applied ML",
                "scores": {"data_science_ml": 3, "ai": 1},
            },
            {
                "label": "Build AI products or research-to-prod systems",
                "scores": {"ai": 3, "data_science_ml": 1},
            },
            {
                "label": "Build connected devices and IoT solutions",
                "scores": {"iot": 3},
            },
            {
                "label": "Work in multimedia / creative tech production",
                "scores": {"multimedia": 3},
            },
        ],
    },
]


def score_answers(selected_indices: list[int]) -> list[tuple[str, int]]:
    """Return quiz career keys ranked by score (highest first). Excludes Other."""
    totals = {key: 0 for key in QUIZ_CAREERS}
    for q, idx in zip(QUESTIONS, selected_indices):
        if idx is None or idx < 0 or idx >= len(q["options"]):
            continue
        for career, points in q["options"][idx]["scores"].items():
            if career in totals:
                totals[career] += points
    return sorted(totals.items(), key=lambda item: item[1], reverse=True)
