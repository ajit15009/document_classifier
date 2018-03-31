class proposal:
	"""docstring for proposal"""
	def __init__(self, data):
		super(proposal, self).__init__()		
		self.p_id=data[0]
		self.teacher_id=data[1]
		self.teacher_prefix=data[2]
		self.school_state=data[3]
		self.project_submission_time=data[4]
		self.project_grade_category=data[5]
		self.project_subject_categories=data[6]
		self.project_subject_sub_categories=data[7]
		self.project_title=data[8]
		self.project_essay_1=data[9]
		self.project_essay_2=data[10]
		self.project_essay_3=data[11]
		self.project_essay_4=data[12]
		self.project_resource_summary=data[13]
		self.teacher_number_of_previously_posted_projects=data[14]
		self.project_is_approved=data[15]

	def __str__(self):
		return str(self.project_title)
		