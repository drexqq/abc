from django.shortcuts import render

# Create your views here.
# load main.html    
def main(request):
    return render(request, 'main.html')

# load board
def board(request):
    return render(request, 'page/board.html')

# load sns
def sns(request):
    return render(request, 'page/sns.html')

# load coin list