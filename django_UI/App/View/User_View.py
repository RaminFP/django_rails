from django.shortcuts import render

# <name.html>_Show
# <name.html>_Index
# <name.html>_Profil

class User_View():

    def User_Show(self,request):

        return render(request, 'Users/User.html')