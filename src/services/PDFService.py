from fpdf import FPDF
from src.models.Cv import Cv
from src.models.Header import Header
from src.models.Experience import Experience
from src.models.Education import Education
from src.models.Certificate import Certificate
from src.models.Award import Award
from datetime import datetime
from math import floor

class ResumePDF(FPDF):
    """Base class to ensure headers and footers are no included in the pdf.

    Args:
        FPDF (_type_): Original FDPF class.
    """
    def header(self):
        pass

    def footer(self):
        pass

class PDFService:
    def __init__(self):
        self.pdf = None
        self.date_format = "%b %Y"

    def generatePDFFromResume(self, title: str, author: str, resume: Cv, output: str):
        """Generates a PDF document from a resume object and saves it to a file at the output location.

        Args:
            title (str): The title of the resume.
            author (str): The author of the resume.
            resume (Cv): The resume object.
            output (str): The file path to save the generated PDF to.
        """
        self.pdf = ResumePDF(orientation="P", unit="mm", format="Letter")
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.set_title(title)
        self.pdf.set_author(author)
        self.pdf.add_page()
        self.pdf.set_font("Helvetica", "", 10)
        self.generateHeader(resume.header)
        self.hr()
        self.generateSummary(resume.summary)
        self.generateSkills(resume.skills)
        self.generateExperience(resume.workExperience)
        self.generateEducation(resume.education)
        self.generateCertifications(resume.certificates)
        self.generateAwards(resume.awards)
        self.pdf.output(output)
        self.pdf = None

    def getRemainingSpace(self) -> float:
        """Get the remaining available space in the document.

        Returns:
            float: The remaining available space left in the document.
        """
        return self.pdf.eph + self.pdf.t_margin - self.pdf.get_y()

    def determinePageBreak(self, height: float):
        """Determine if a page break is necessary based on the provided height requested by a section.

        Args:
            height (float): The height of the section that wants to be placed.
        """
        remaining_space = self.getRemainingSpace()
        if height > remaining_space:
            self.pdf.add_page()

    def calculateMultiCellHeight(self, text: str, cell_height: int, indent: int = 0) -> float:
        """Calculate the height of a multicell with the supplied arguments.
        Height is calculated from word based text wrapping.

        Args:
            text (str): The text for the multicell.
            cell_height (int): The height of each cell line in the multicell.
            indent (int, optional): The size of the indent, if any. Defaults to 0.

        Returns:
            float: The total height of the multicell.
        """
        line_count = 1
        current_line_width = indent
        for word in text.split(" "):
            word_width = self.pdf.get_string_width(f"{word} ")
            if current_line_width + word_width > self.pdf.epw:
                line_count += 1
                current_line_width = 0
            current_line_width += word_width
        return float(line_count * cell_height)

    def hr(self, gap_before=2, gap_after=4):
        """Adds a horizontal rule on the current pdf being generated.

        Args:
            gap_before (int, optional): Gap before rule. Defaults to 2.
            gap_after (int, optional): Gap after rule. Defaults to 4.
        """
        self.pdf.ln(gap_before)
        x1 = self.pdf.l_margin
        x2 = self.pdf.w - self.pdf.r_margin
        y = self.pdf.get_y()
        self.pdf.set_line_width(0.2)
        self.pdf.line(x1, y, x2, y)
        self.pdf.ln(gap_after)

    def sectionTitle(self, title: str):
        """Adds a section title to the current pdf being generated.

        Args:
            title (str): The title of the section.
        """
        self.pdf.set_font("Helvetica", "B", 11)
        self.pdf.ln(2)
        self.pdf.cell(0, 6, title.upper(), ln=1, align="L")
        self.pdf.set_font("Helvetica", "", 10)

    def bullet(self, text: str, indent: int = 4):
        """Adds a bullet point to the current pdf being generated.

        Args:
            text (str): The text to include next to the bullet point.
            indent (int, optional): The indent for this bullet point. Defaults to 4.
        """
        self.pdf.set_x(self.pdf.l_margin + indent)
        self.pdf.multi_cell(0, 5, f"- {text}", align="L")

    def generateHeader(self, header: Header):
        """Generates and formats the header section.

        Args:
            header (Header): Resume header object.
        """
        info_cell_1 = ""
        info_cell_2 = ""
        location_part = ""
        for x in [header.city, header.state, header.country]:
            if x:
                location_part += f"{x}, "
        if location_part:
            info_cell_1 += f"{location_part[0:-2]}  |  "
        for x in [header.phoneNumber, header.email]:
            if x:
                info_cell_1 += f"{x}  |  "
        for x in [header.website, header.altWebsite]:
            if x:
                info_cell_2 += f"{x}  |  "

        self.pdf.set_font("Helvetica", "B", 16)
        self.pdf.cell(0, 8, header.name, ln=1, align="L")

        self.pdf.set_font("Helvetica", "I", 10)
        self.pdf.cell(0, 5, header.profession, ln=1, align="L")

        self.pdf.set_font("Helvetica", "", 10)
        self.pdf.cell(0, 5, info_cell_1[0:-5], ln=1, align="L")
        if info_cell_2:
            self.pdf.cell(0, 5, info_cell_2[0:-5], ln=1, align="L")

    def generateSummary(self, summary: str):
        """Generates and formats the resume summary.

        Args:
            summary (str): The summary from the resume.
        """
        if summary:
            self.sectionTitle("Summary")
            self.pdf.multi_cell(
                0,
                5,
                summary,
                align="L"
            )

    def generateSkills(self, skills: list[str]):
        """Generates and formats the skills section.

        Args:
            skills (list[str]): List of skills.
        """
        if len(skills) > 0:
            self.sectionTitle("Skills")
            skill_str = ""
            for x in skills:
                skill_str += f"{x}, "
            self.pdf.multi_cell(0, 5, skill_str[0:-2], align="L")

    def generateExperience(self, experience: list[Experience]):
        """Generates and formats the work experience section.

        Args:
            experience (list[Experience]): List of work experience objects.
        """
        def calculateSingleWorkSectionHeight(w: Experience) -> float:
            h = 13.0
            for b in w.bullets:
                h += self.calculateMultiCellHeight(b.text, 5, 4)
            return h

        if len(experience) > 0:
            self.determinePageBreak(
                8.0 + calculateSingleWorkSectionHeight(experience[0])
            )
            self.sectionTitle("Experience")
            for i, work in enumerate(experience):
                if i != 0:
                    self.determinePageBreak(calculateSingleWorkSectionHeight(work))

                self.pdf.set_font("Helvetica", "B", 10)
                self.pdf.cell(0, 5, work.jobTitle, ln=1, align="L")
                self.pdf.set_font("Helvetica", "", 10)
                strWorkStarted = datetime.strftime(work.startedOn, self.date_format)
                if work.currentPosition:
                    timeframe = f"{strWorkStarted} - present"
                else:
                    timeframe = f"{strWorkStarted} - {datetime.strftime(work.endedOn, self.date_format)}"
                self.pdf.cell(
                    0,
                    5,
                    f"{work.company}  |  {work.companyLocation}  |  {timeframe}",
                    ln=1,
                    align="L",
                )
                self.pdf.ln(1)
                for bullet in work.bullets:
                    self.bullet(bullet.text)
                self.pdf.ln(2)

    def generateEducation(self, education: list[Education]):
        """Generates and formats the education section.

        Args:
            education (list[Education]): List of education objects.
        """
        if len(education) > 0:
            self.determinePageBreak(8.0 + 10.0 * len(education))
            self.sectionTitle("Education")
            for edu in education:
                self.pdf.set_font("Helvetica", "B", 10)
                formatted_degree = f"{edu.degreeType.name[0].upper()}{edu.degreeType.name[1:].lower()}"
                self.pdf.cell(
                    0, 5, f"{formatted_degree} - {edu.major}", ln=1, align="L"
                )
                self.pdf.set_font("Helvetica", "", 10)
                if edu.stillAttending:
                    str_grad_phrase = "Expected Graduation"
                else:
                    str_grad_phrase = "Graduated"
                self.pdf.cell(
                    0,
                    5,
                    f"{edu.schoolName}  |  {str_grad_phrase}: {datetime.strftime(edu.graduationDate, self.date_format)}",
                    ln=1,
                    align="L",
                )

    def generateCertifications(self, certifications: list[Certificate]):
        """Generates and formats the certifications section.

        Args:
            certifications (list[Certificate]): List of certification objects.
        """
        if len(certifications) > 0:
            self.determinePageBreak(8.0 + 5.0 * len(certifications))
            self.sectionTitle("Certifications")
            for cert in certifications:
                if cert.doesNotExpire:
                    str_expiration = ""
                else:
                    str_expiration = f"  |  Expires: {datetime.strftime(cert.expDate, self.date_format)}"
                self.pdf.cell(
                    0,
                    5,
                    f"{cert.issuer} {cert.certificateName}  |  Issued: {datetime.strftime(cert.issueDate, self.date_format)}{str_expiration}",
                    ln=1,
                    align="L",
                )

    def generateAwards(self, awards: list[Award]):
        """Generates and formats the awards section.

        Args:
            awards (list[Award]): List of award objects.
        """
        if len(awards) > 0:
            self.determinePageBreak(8.0 + 5.0 * len(awards))
            self.sectionTitle("Awards")
            for award in awards:
                self.pdf.cell(
                    0,
                    5,
                    f"{award.awardName}  |  {award.issuer}  |  Issued: {datetime.strftime(award.issueDate, self.date_format)}",
                    ln=1,
                    align="L"
                )
