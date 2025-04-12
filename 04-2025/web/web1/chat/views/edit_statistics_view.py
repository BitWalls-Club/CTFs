from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
import os
from django.conf import settings
from django.template import engines

def is_admin(user):
    return user.username == "admin"

@login_required
@user_passes_test(is_admin)
def EditStatsView(request):
    success_message = None
    error_message = None
    stats_path = os.path.join(settings.TEMPLATES[0]["DIRS"][0], "statistics.html")
    
    if request.method == "POST":
        new_content = request.POST.get("html_content", "")
        try:
            with open(stats_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            success_message = "Statistics page updated successfully."
            
            # Clear Django template cache
            for engine in engines.all():
                if hasattr(engine, 'engine'):
                    for loader in engine.engine.template_loaders:
                        if hasattr(loader, 'cache'):
                            loader.cache.clear()
            
        except Exception as e:
            error_message = f"Failed to update: {str(e)}"
    
    # Load current content and strip newlines
    current_html = ""
    try:
        with open(stats_path, "r", encoding="utf-8") as f:
            current_html = f.read().replace("\n", "")  # remove newlines
    except Exception as e:
        error_message = f"Unable to load statistics file: {str(e)}"
    
    return render(request, "edit_statistics.html", {
        "html_content": current_html,
        "success_message": success_message,
        "error_message": error_message
    })
