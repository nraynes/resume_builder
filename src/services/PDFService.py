from fpdf import FPDF
from src.models.Resume import Resume
from src.models.Header import Header
from src.models.Experience import Experience
from src.models.Education import Education
from src.models.Certificate import Certificate
from datetime import datetime

class ResumePDF(FPDF):
    def header(self):
        pass

    def footer(self):
        pass

class PDFService:
    def __init__(self):
        self.pdf = None
        self.date_format = "%b %Y"

    def generatePDFFromResume(self, resume: Resume, output: str):
        self.pdf = ResumePDF(orientation="P", unit="mm", format="Letter")
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.set_title(resume.title)
        self.pdf.set_author(resume.author)
        self.pdf.add_page()
        self.pdf.set_font("Helvetica", "", 10)
        self.generateHeader(resume.header)
        self.hr()
        self.generateSummary(resume.summary)
        self.generateSkills(resume.skills)
        self.generateExperience(list(resume.workExperience.values()))
        self.generateEducation(list(resume.education.values()))
        self.generateCertifications(list(resume.certificates.values()))
        self.pdf.output(output)
        self.pdf = None

    def hr(self, gap_before=2, gap_after=4):
        self.pdf.ln(gap_before)
        x1 = self.pdf.l_margin
        x2 = self.pdf.w - self.pdf.r_margin
        y = self.pdf.get_y()
        self.pdf.set_line_width(0.2)
        self.pdf.line(x1, y, x2, y)
        self.pdf.ln(gap_after)

    def section_title(self, title: str):
        self.pdf.set_font("Helvetica", "B", 11)
        self.pdf.ln(2)
        self.pdf.cell(0, 6, title.upper(), ln=1)
        self.pdf.set_font("Helvetica", "", 10)

    def bullet(self, text: str, indent=4):
        self.pdf.set_x(self.pdf.l_margin + indent)
        self.pdf.multi_cell(0, 5, f"- {text}")

    def generateHeader(self, header: Header):
        self.pdf.set_font("Helvetica", "B", 16)
        self.pdf.cell(0, 8, header.name, ln=1)

        self.pdf.set_font("Helvetica", "I", 10)
        self.pdf.cell(0, 5, header.profession, ln=1)

        self.pdf.set_font("Helvetica", "", 10)
        info_cell = ""
        location_part = ""
        for x in [header.city, header.state, header.country]:
            if x:
                location_part += f"{x}, "
        if location_part:
            info_cell += f"{location_part[0:-2]}  |  "
        for x in [header.phoneNumber, header.email, header.website, header.altWebsite]:
            if x:
                info_cell += f"{x}  |  "
        self.pdf.cell(0, 5, info_cell[0:-5], ln=1)

    def generateSummary(self, summary: str):
        if summary:
            self.section_title("Summary")
            self.pdf.multi_cell(
                0,
                5,
                summary,
            )

    def generateSkills(self, skills: list[str]):
        if len(skills) > 0:
            self.section_title("Skills")
            skill_str = ""
            for x in skills:
                skill_str += f"{x}, "
            self.pdf.multi_cell(0, 5, skill_str[0:-2])

    def generateExperience(self, experience: list[Experience]):
        if len(experience) > 0:
            self.section_title("Experience")

            for job in experience:
                self.pdf.set_font("Helvetica", "B", 10)
                self.pdf.cell(0, 5, job.jobTitle, ln=1)
                self.pdf.set_font("Helvetica", "", 10)
                if job.currentPosition:
                    timeframe = f"{datetime.strftime(job.startedOn, self.date_format)} - present"
                else:
                    timeframe = f"{datetime.strftime(job.startedOn, self.date_format)} - {datetime.strftime(job.endedOn, self.date_format)}"
                self.pdf.cell(
                    0,
                    5,
                    f"{job.company}  |  {job.companyLocation}  |  {timeframe}",
                    ln=1,
                )
                self.pdf.ln(1)
                for bullet in job.bullets.values():
                    self.bullet(bullet["text"])
                self.pdf.ln(2)

    def generateEducation(self, education: list[Education]):
        if len(education) > 0:
            self.section_title("Education")
            for edu in education:
                self.pdf.set_font("Helvetica", "B", 10)
                self.pdf.cell(0, 5, f"{edu.degreeType} - {edu.major}", ln=1)
                self.pdf.set_font("Helvetica", "", 10)
                if edu.stillAttending:
                    grad = "Expected Graduation"
                else:
                    grad = "Graduated"
                self.pdf.cell(0, 5, f"{edu.schoolName}  |  {grad}: {datetime.strftime(edu.graduationDate, self.date_format)}", ln=1)

    def generateCertifications(self, certifications: list[Certificate]):
        if len(certifications) > 0:
            self.section_title("Certifications")
            for cert in certifications:
                if cert.doesNotExpire:
                    exp_date = ""
                else:
                    exp_date = f" - {datetime.strftime(cert.expDate, self.date_format)}"
                self.pdf.multi_cell(
                    0,
                    5,
                    f"{cert.issuer} {cert.certificateName}  |  {datetime.strftime(cert.issueDate, self.date_format)}{exp_date}",
                )
