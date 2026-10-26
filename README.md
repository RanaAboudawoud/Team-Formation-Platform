# PA1414 Software Engineering Project HT26

## Project Description

**Project Name:** *Team Formation Platform*

**Customer Name:** *Zeth Danielsson ZDA*

**Student Full Name:** *Rana Aboudawoud*

### Project Aim and Objectives

*This is a platform where collaboration and team-building is made easier. An idea-maker and a potential team-memeber match together based on skills and requirements. No longer should you be bothered by useless notifications and applicants, now - notifications matter.*

### User Personas

#### Alice - Collaborator

| Name | Characteristics | Needs and Expectations | How will they use the system? |
| --- | --- | --- | --- |
| **Alice** | 24, CS major, intermediate at programming.<br><br>Knows JavaScript and Python.<br><br>Open to learning new techniques/languages.<br><br>Alice is nearing the end of her studies and wants practical experience but does not currently have a project idea of her own.<br><br>Has limited availability because of her studies. | Find a project she can contribute to and gain experience from.<br><br>Get relevant projects recommended based on her skills and availability.<br><br>Be able to understand why a project is a good match for her.<br><br>Not get contacted by people she has not shown interest in. | Create a profile and list her skills, programming languages, proficiency and availability.<br><br>Get recommended projects based on her profile.<br><br>Look through the recommendations and see why they match.<br><br>Express interest in one or multiple projects.<br><br>Start communicating with the Idea Maker if they both show interest. |

#### Stefan - Idea Maker

| Name | Characteristics | Needs and Expectations | How will they use the system? |
| --- | --- | --- | --- |
| **Stefan** | 37, entrepreneur with experience in business development.<br><br>Has an idea for a digital service but does not have all the technical skills needed to build it.<br><br>Does not have suitable collaborators in his network.<br><br>Does not want to share too much about his idea before finding the right people. | Find people with the right skills and availability for his project.<br><br>See which candidates are the best match and why.<br><br>Be able to decide what is more important in the matching, for example skills or availability.<br><br>Control how much information about his idea is public. | Create a profile.<br><br>Make a post about his idea and what stage it is in.<br><br>List what roles and skills he needs.<br><br>See ranked candidates and why they match his project.<br><br>Change the matching priorities if needed.<br><br>See who has shown interest in his idea and show interest in suitable candidates.<br><br>Start communicating when the interest is mutual. |

### Software Requirements

#### Functional Requirements

| ID | Requirement |
| --- | --- |
| FR-01 | Users should be able to create an account and profile. |
| FR-02 | Collaborators should be able to list their skills and how experienced they are with them. |
| FR-03 | Collaborators should be able to list their availability, commitment and what kind of projects they are interested in. |
| FR-04 | Idea Makers should be able to post an idea and describe what they are building and how far along the project is. |
| FR-05 | Idea Makers should be able to list what roles and skills they need for their project. |
| FR-06 | The system should recommend suitable ideas to Collaborators based on skills, availability, interests and commitment. |
| FR-07 | Collaborators should be shown ideas ranked by how well they fit their profile. |
| FR-08 | Collaborators should be able to choose if they want to show interest in an idea. |
| FR-09 | Idea Makers should be able to see Collaborators who have shown interest in their idea. |
| FR-10 | Collaborators who have shown interest should be ranked by how well they fit the project. |
| FR-11 | The system should explain why an idea or interested Collaborator got its ranking. |
| FR-12 | Idea Makers should be able to change how important different parts of the ranking are, for example skills or availability. |
| FR-13 | The ranking should change when the matching weights are changed. |
| FR-14 | Idea Makers should be able to choose if they want to show interest in a Collaborator who has already shown interest in their idea. |
| FR-15 | A match should only happen when both sides have chosen to show interest. |
| FR-16 | Users should be able to chat after they have matched. |
| FR-17 | Idea Makers should be able to choose what information about their idea is public and what information is only shown after mutual interest. |
| FR-18 | Idea Makers should be able to see which skills are still missing from their team. |

#### Non-Functional Requirements

| ID | Category | Requirement |
| --- | --- | --- |
| NFR-01 | Security | Users should not be able to see information they are not allowed to see. |
| NFR-02 | Privacy | Private information about an idea should only be visible to users who are allowed to see it. |
| NFR-03 | Privacy | A Collaborator's profile should not be visible to an Idea Maker unless the Collaborator has shown interest in that Idea Maker's project. |
| NFR-04 | Privacy | Users should not be able to contact each other before both sides have shown interest. |
| NFR-05 | Performance | The system should still work well when there are many ideas or interested Collaborators. |
| NFR-06 | Performance | Long lists of ideas or interested Collaborators should be handled in a way that keeps the system usable. If there are more than 20 then the list should be paginated|
| NFR-07 | Usability | Users should be able to understand why a match got its ranking. |
| NFR-08 | Availability | The system should be available online 99% of the time when deployed as a web application. |

---

## User manual

### Installing
1. Clone the repo
2. Go into project folder
3. Create virtual environment:
    - python -m venv venv
4. Activate the virtual environment
    - For windows users:
        - venv\Scripts\avticate
    - For macos/linux users:
        - source venv/bin/activate
5. Install django
    - pip install Django==6.1.1
6. Run the database migrations
    - python manage.py migrate

### Running
1. Start the server
    - python manage.py runserver
2. Open in browser with this url
    - http://127.0.0.1:8000/

