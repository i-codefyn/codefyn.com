AOS.init({easing:'ease-in-out-sine'});;$(document).ready(function(){$(".preloader").hide();$("#MainForm").on("submit",function(){$(".preloader").fadeIn();});});function logoutFunction(){swal.fire({title:"Sure Want to Logout ?",type:"warning",showCancelButton:true,confirmButtonColor:"#3085d6",cancelButtonColor:"#d33",confirmButtonText:"OK",closeOnConfirm:true,closeOnCancel:false,}).then((result)=>{if(result.value===true){$("#logoutform").submit();}});}
function confirmFunction(){event.preventDefault();var form=event.target.form;Swal.fire({title:"Are you sure?",text:"Want to logout!",type:"warning",showCancelButton:true,confirmButtonColor:"#f00000",cancelButtonColor:"#333",confirmButtonText:"Yes,Logout!",}).then((result)=>{if(result.value){form.submit();}});}
var navItems=document.querySelectorAll(".bloc-icon");navItems.forEach(function(e,i){e.addEventListener("click",function(e){navItems.forEach(function(e2,i2){e2.classList.remove("block-icon-active");});this.classList.add("block-icon-active");});});(function(){"use strict";var tooltipTriggerList=[].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));tooltipTriggerList.forEach(function(tooltipTriggerEl){new bootstrap.Tooltip(tooltipTriggerEl);});})();$(document).ready(function(){$("#sidebarCollapse").on("click",function(){$("#sidebar").addClass("active");});$("#sidebarCollapseX").on("click",function(){$("#sidebar").removeClass("active");});$("#sidebarCollapse").on("click",function(){if($("#sidebar").hasClass("active")){$(".overlay").addClass("visible");console.log("it's working!");}});$("#sidebarCollapseX").on("click",function(){$(".overlay").removeClass("visible");});});var tooltipTriggerList=[].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));var tooltipList=tooltipTriggerList.map(function(tooltipTriggerEl){return new bootstrap.Tooltip(tooltipTriggerEl);});document.addEventListener("DOMContentLoaded",function(){window.addEventListener("scroll",function(){if(window.scrollY>50){document.getElementById("navbar_top").classList.add("is-scrolling");navbar_height=document.querySelector(".navbar").offsetHeight;document.body.style.paddingTop=navbar_height+"px";}else{document.getElementById("navbar_top").classList.remove("is-scrolling");document.body.style.paddingTop="0";}});});(function(window,$,undefined){"use strict";$(document).ready(function(){function is_scrolling(){var $element=$(".site-header"),$nav_height=$element.outerHeight(true);if($(this).scrollTop()>=$nav_height){$element.addClass("is-scrolling");}else{$element.removeClass("is-scrolling");}}
$(window).scroll(_.throttle(is_scrolling,200));});})(this,jQuery);(function(){"use strict";var forms=document.querySelectorAll(".needs-validation");Array.prototype.slice.call(forms).forEach(function(form){form.addEventListener("submit",function(event){if(!form.checkValidity()){event.preventDefault();event.stopPropagation();}
form.classList.add("was-validated");},false);});})();window.addEventListener('load',()=>{let portfolioContainer=select('.portfolio-container');if(portfolioContainer){let portfolioIsotope=new Isotope(portfolioContainer,{itemSelector:'.portfolio-item',layoutMode:'fitRows'});let portfolioFilters=select('#portfolio-flters li',true);on('click','#portfolio-flters li',function(e){e.preventDefault();portfolioFilters.forEach(function(el){el.classList.remove('filter-active');});this.classList.add('filter-active');portfolioIsotope.arrange({filter:this.getAttribute('data-filter')});portfolioIsotope.on('arrangeComplete',function(){AOS.refresh()});},true);}});const portfolioLightbox=GLightbox({selector:'.portfolio-lightbox'});new Swiper('.portfolio-details-slider',{speed:400,loop:true,autoplay:{delay:5000,disableOnInteraction:false},pagination:{el:'.swiper-pagination',type:'bullets',clickable:true}});;