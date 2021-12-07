
class Categories:
    def __init__(self, one_run):
        parameters = one_run.split(',')
        self.city = parameters[0]
        self.intervention = parameters[1]
        if "ASCENDING" in one_run:
            self.order = "ASCENDING"
        elif "DESCENDING" in one_run:
            self.order = "DESCENDING"
        else:
            self.order = "NONE"
        if "HOUSEHOLDS_ALL_AT_ONCE" in one_run:
            self.vaccination_strategy = "HH_ALL_AT_ONCE"
        elif "HOUSEHOLD" in one_run:
            self.vaccination_strategy = "HOUSEHOLD"
        elif "BY_NEIGHBORHOOD" in one_run:
            self.vaccination_strategy = "BY_NEIGHBORHOOD"
        elif "GENERAL" in one_run:
            self.vaccination_strategy = "GENERAL"
        else:
            print(f"ERROR! unknown order! in {one_run}")
            exit(-1)
        self.immune_per_day = 0
        self.initial_infected = 0
        for i in range(len(parameters)):
            if 'imm_per_day' in parameters[i]:
                self.immune_per_day = parameters[i].split('=')[1]
            if 'inf=' in parameters[i]:
                self.initial_infected = parameters[i].split('=')[1]
            if 'comp=' in parameters[i]:
                self.compliance = parameters[i].split('=')[1]

    def __str__(self):
        return f"{self.city}\nINF={self.initial_infected}\nIMMUNE={self.immune_per_day}\n" \
               f"{self.vaccination_strategy}\n{self.order}\ncompliance={self.compliance}"
