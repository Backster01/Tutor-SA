# Building a Tutoring App with GitHub Copilot agent mode for Matilda's Tutoring

## Tutor SA application story for Matilda's Tutoring

Matilda has been a foundation phase education teacher for over 28 years. Despite her enthusiasm and creative approach to teach her students, she's been increasingly concerned about students' ability to cope with their school work. Many students admitted they struggel to keep up with the work during classes.
After attending a professional development conference on "Technology Integration in Education assistance teaching," Matilda became inspired to create a solution for South African CAPS-aligned tutoring app! A comprehensive educational platform tailored specifically for the South African curriculum will be incredibly valuable for students, teachers, parents, and tutors. She wanted something that would:

1. Make Tutoring fun and engaging
2. Create positive attitude and willingness to study with the interactive Tutoring App 
3. Allow her to monitor student progress remotely with assesements and short quize's after each session.
4. Provide personalized guidance based on individual progress levels

## The Birth of Tutoring SA

Matilda initially sketched her idea on a notepad during lunch breaks. He envisioned an app where students could improve their knowledge, earn achievement badges. However, as a teacher with only basic coding knowledge, the technical aspects seemed daunting.
That's when she approached Johannes, IT teacher. Johannes recommended basing the app on the South Africa CAPS, which was documented in `docs/totur-sa.md`. She saw potential in adapting the Tutoring app to the CAPS standards.

### Technical Planning Phase

Before starting development, Matilda and Johannes carefully reviewed the CAPS repository and documentation. They provided a solid foundation for Tutoring SA, ensuring compliance with technical standards and leveraging proven design patterns.
Together, Matilda and the IT team identified key requirements for Tutoring SA:

### User Experience Goals

- Simple, intuitive interface designed specifically for teenagers
- Quick activity logging to minimize friction
- Social features that respect student privacy
- Gamification elements to maintain engagement

### Technical Specifications

- Mobile-responsive web application (accessible on school Chromebooks and personal devices)
- Secure authentication and user enrolment and logging in (Student, Teacher, Parent, Admin/Tutor)
- Activity verification system to prevent cheating

## Current Development Status

Matilda and Johannes have set up a GitHub Codespace environment and are making remarkable progress with GitHub Copilot agent mode. By adapting the Tutoring SA's structure:

- A functional user registration system
- User authentication system with different roles (Student, Teacher, Parent, Admin/Tutor)
- Dashboard interfaces tailored to each user type
- CAPS curriculum structure organized by grade levels and subjects
- Basic lesson viewing functionality
- Assessment system with progress tracking


## Next Steps for Matilda

With the basic infrastructure in place, Matilda is now focused on:

1. CAPS-Aligned Curriculum
2. Interactive Learning Experience
3. Assessment System
4. Content Management System
5. Lesson Management System
6. Assessment Management System
7. Subject Management Pages
8. Content versioning to track changes

The IT department has been impressed with how GitHub Copilot agent mode has accelerated development, allowing Matilda to focus on the educational aspects while the AI handles much of the technical implementation. Johannes has been particularly pleased with how tUTORING SA leverages the CAPS-Aligned foundation to meet the School's unique requirements.

### Workshop Overview

In ther workshop, you'll:

1. Set up a development environment using **GitHub Codespaces**
2. Use **GitHub Copilot** to accelerate development across multiple technologies
3. Build key components of the **Tutoring SA** app with the help of Copilot agent mode
4. Learn best practices and prompting techniques for working with **GitHub Copilot agent mode**

### Application Features

**Tutoring SA** will include:

- User Authentication & Profiles
- CAPS-Aligned Curriculum
- Interactive Learning Experience
- Assessment System
- Content Management System
- Lesson Management System
- Assessment Management System
- Subject Management Pages
- Content versioning to track changess

### GitHub Copilot Chat

These are the current models supported for GitHub Copilot Chat.

- Claude Sonnet 3.5 (Preview)
- Claude Sonnet 3.7 (Preview)
- Claude Sonnet 3.7 Thinking (Preview)
- Gemini 2.0 Flash (Preview)
- GPT-4o
- o1 (Preview)
- o3-mini (Preview)

#### [LLM models explained](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#ai-models-for-copilot-chat-1)

![GitHub Copilot Chat models](https://github.com/user-attachments/assets/f2f8d0bd-366b-4ecf-b88d-d092ae7b8b10)

#### Prompt engineering

- [GitHub documentation prompt engineering](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
- [How to use GitHub Copilot: Prompts, tips, and use cases](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)
- [Using GitHub Copilot in your IDE: Tips, tricks, and best practices](https://github.blog/2024-03-25-how-to-use-github-copilot-in-your-ide-tips-tricks-and-best-practices/)
- [A developer's guide to prompt engineering and LLMs](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot#:~:text=A%20developer%E2%80%99s%20guide%20to%20prompt%20engineering%20and%20LLMs)
- [GitHub Copilot: The Agent Awakens](https://github.blog/news-insights/product-news/github-copilot-the-agent-awakens/#agent-mode-available-in-preview-%f0%9f%a4%96)

### Tutoring SA application technology stack

We'll be using a modern web application stack:

- **Frontend**: React.js
- **Backend**: Python with Django REST Framework
- **Database**: MongoDB
- **Development Environment**: GitHub Codespaces

### Workshop Structure

1. **Introduction**
   - Overview of Tutoring SA app concept
   - GitHub Copilot Chat models

2. **Setup of Prerequisites**
   - Setting up GitHub Codespaces
   - Ensure GitHub Copilot and Copilot Chat extensions are up to date

3. **Rapid Prototyping with GitHub Copilot agent mode**
   - Creating project structure
   - Generating boilerplate code
   - Implementing basic models, serializers, URLs, and views

4. **Building Core Features**
- User Authentication & Profiles
   •	Individual login for each student
   •	Age-appropriate user interfaces based on grade level
   •	Profile tracking for progress monitoring
   •	Parental/teacher access options for monitoring
- CAPS-Aligned Curriculum
   •	Complete coverage of all subjects from Grade R to Grade 12
   •	Dedicated modules for language subjects (English and Afrikaans)
   •	Content organized by grade, subject, and learning unit
   •	Updatable database structure to accommodate curriculum changes
- Interactive Learning Experience
   •	Age-appropriate interfaces for different grade levels
   •	Gamification elements tailored by age group
   •	Multimedia content (videos, animations, interactive exercises)
   •	Voice-guided learning for younger students
- Assessment System
   •	Section-end quizzes/tests
   •	Varied question formats (multiple choice, fill-in-blank, problem-solving)
   •	Immediate feedback mechanisms
   •	Difficulty adjustment based on performance
- Progress Tracking & Reporting
   •	Continuous progress monitoring
   •	Quarterly detailed reports
   •	Year-end comprehensive assessment
   •	Visual progress dashboards for students and parents
   •	Identification of strengths and areas needing improvement
- Content Management System
   •	Centralized CAPS curriculum database (PDFs, Excel, PowerPoint, Word) documents
   •	Regular update mechanism for curriculum changes
- Lesson Management System
   o	Lesson Listing Page: View all lessons with filtering by subject and search functionality
   o	Lesson Creation Page: Create new lessons with title, content, and subject selection
   o	Lesson Detail Page: View complete lesson content with subject and teacher information
   o	Lesson Edit Page: Update existing lesson content and details
- Assessment Management System
   o	Students to view their assessments and track their progress
   o	Teachers to create, view, edit, and delete assessments for their subjects
   o	Teachers to grade assessments by setting scores and marking them as completed
   o	Admins to manage all assessments across the platform
- Subject Management Pages
   o	Subject Listing Page: A page that displays all subjects with filtering by grade levels (Foundation, Intermediate, Senior, and FET phases)
   o	Subject Creation Form: A form for teachers and admins to create new subjects
   o	Subject Edit Page: A page to modify existing subjects
   o	Subject Detail Page: A detailed view of a subject with tabs for overview, lessons, and students
- Content versioning to track changes


5. **Frontend and Backend Development**
   - Setting up React components
   - Implementing responsive UI
   - Connecting to backend APIs
   - Python Django business logic
   - MongoDB data layer
