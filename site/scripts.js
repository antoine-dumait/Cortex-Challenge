document.getElementById("calcul-nav").addEventListener("click", () => showProblem("calcul"));
document.getElementById("couleur-nav").addEventListener("click", () => showProblem("couleur"));
document.getElementById("doublon-nav").addEventListener("click", () => showProblem("doublon"));
document.getElementById("frequence-nav").addEventListener("click", () => showProblem("frequence"));
document.getElementById("labyrinthe-nav").addEventListener("click", () => showProblem("labyrinthe"));
document.getElementById("manquant-nav").addEventListener("click", () => showProblem("manquant"));
document.getElementById("raisonnement-nav").addEventListener("click", () => showProblem("raisonnement"));
document.getElementById("reflexion-nav").addEventListener("click", () => showProblem("reflexion"));
document.getElementById("preface-nav").addEventListener("click", () => showProblem("preface"));

current_problem = "preface";
problem_bg = "#457b9d"
hover_bg = "#1f4a65"
function showProblem(problem){
    console.log(problem);
    if (problem != current_problem){
    document.getElementById(current_problem).style.display = "none";
    document.getElementById(current_problem+"-nav").parentNode.style.backgroundColor = problem_bg;
    document.getElementById(problem).style.display = "block";
    document.getElementById(problem+"-nav").parentNode.style.backgroundColor = hover_bg;
    current_problem = problem;}
}