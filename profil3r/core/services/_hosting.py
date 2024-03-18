from profil3r.modules.hosting.aboutme import AboutMe

# AboutMe
def aboutme(self):
    self.result["aboutme"] = AboutMe(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("aboutme")
