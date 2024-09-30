from dataclasses import dataclass

<<<<<<< HEAD
=======
from loguru import logger


>>>>>>> e1d1ea8534f538bd20053e26f4f379adeef0eca4
@dataclass
class Job:
    title: str
    company: str
    location: str
    link: str
    apply_method: str
    description: str = ""
    summarize_job_description: str = ""
    pdf_path: str = ""
    recruiter_link: str = ""

    def set_summarize_job_description(self, summarize_job_description):
<<<<<<< HEAD
        self.summarize_job_description = summarize_job_description

    def set_job_description(self, description):
        self.description = description

    def set_recruiter_link(self, recruiter_link):
=======
        logger.debug(f"Setting summarized job description: {summarize_job_description}")
        self.summarize_job_description = summarize_job_description

    def set_job_description(self, description):
        logger.debug(f"Setting job description: {description}")
        self.description = description

    def set_recruiter_link(self, recruiter_link):
        logger.debug(f"Setting recruiter link: {recruiter_link}")
>>>>>>> e1d1ea8534f538bd20053e26f4f379adeef0eca4
        self.recruiter_link = recruiter_link

    def formatted_job_information(self):
        """
        Formats the job information as a markdown string.
        """
<<<<<<< HEAD
=======
        logger.debug(f"Formatting job information for job: {self.title} at {self.company}")
>>>>>>> e1d1ea8534f538bd20053e26f4f379adeef0eca4
        job_information = f"""
        # Job Description
        ## Job Information 
        - Position: {self.title}
        - At: {self.company}
        - Location: {self.location}
        - Recruiter Profile: {self.recruiter_link or 'Not available'}
        
        ## Description
        {self.description or 'No description provided.'}
        """
<<<<<<< HEAD
        return job_information.strip()
=======
        formatted_information = job_information.strip()
        logger.debug(f"Formatted job information: {formatted_information}")
        return formatted_information
>>>>>>> e1d1ea8534f538bd20053e26f4f379adeef0eca4
