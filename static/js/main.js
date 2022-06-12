var 
  tabButton = document.querySelectorAll(".product .navTab .nav-tabs .nav-link"),
  tabox     = document.querySelectorAll(".product .box-content");
  console.log(tabButton);
  console.log(tabox);
  tabox.forEach(function(node){
    node.style.opactiy = "0";
    node.style.transition = "all 0.2s ease-in";
    node.style.display = "none";
  });
  tabox[0].style.display = "block";
  // function showpanel v1.0
  function showpanel(index){
    tabox.forEach(function(node){
      node.style.opactiy = "0";
      node.style.transition = "all 0.2s ease-in";
      node.style.transform = "translateX(157px)";
      setTimeout(function(){
        node.style.display = "none";
      }, 80);
    });
    tabButton.forEach(function(node){
      node.style.transition = "all 0.2s ease-in";
      node.style.background = "#D8D3CE";
      node.style.color = "#444343";
      node.style.transition = "all 0.2s ease-in";
    });
    console.log(tabox[index]);
    setTimeout(function(){
      tabox[index].style.opacity = "1";
      tabox[index].style.transition = "all 0.2s ease-in";
      tabox[index].style.transform = "translateX(0px)";
      tabox[index].style.display = "block";
    }, 80);
    tabButton[index].style.background = "linear-gradient(0deg, #fc544c 0%, #f03755 100%)";
    tabButton[index].style.color = "#fff";
    tabox[index].style.transition = "all 0.2s ease-in";
  }