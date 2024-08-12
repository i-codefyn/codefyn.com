AOS.init({easing:'ease-in-out-sine'});(function(){"use strict";const select=(el,all=false)=>{el=el.trim()
if(all){return[...document.querySelectorAll(el)]}else{return document.querySelector(el)}}
const on=(type,el,listener,all=false)=>{let selectEl=select(el,all)
if(selectEl){if(all){selectEl.forEach(e=>e.addEventListener(type,listener))}else{selectEl.addEventListener(type,listener)}}}
const onscroll=(el,listener)=>{el.addEventListener('scroll',listener)}
let navbarlinks=select('#navbar .scrollto',true)
const navbarlinksActive=()=>{let position=window.scrollY+200
navbarlinks.forEach(navbarlink=>{if(!navbarlink.hash)return
let section=select(navbarlink.hash)
if(!section)return
if(position>=section.offsetTop&&position<=(section.offsetTop+section.offsetHeight)){navbarlink.classList.add('active')}else{navbarlink.classList.remove('active')}})}
window.addEventListener('load',navbarlinksActive)
onscroll(document,navbarlinksActive)
const scrollto=(el)=>{let header=select('#header')
let offset=header.offsetHeight
if(!header.classList.contains('header-scrolled')){offset-=20}
let elementPos=select(el).offsetTop
window.scrollTo({top:elementPos-offset,behavior:'smooth'})}
let selectHeader=select('#header')
if(selectHeader){const headerScrolled=()=>{if(window.scrollY>100){selectHeader.classList.add('header-scrolled')}else{selectHeader.classList.remove('header-scrolled')}}
window.addEventListener('load',headerScrolled)
onscroll(document,headerScrolled)}
let heroCarouselIndicators=select("#hero-carousel-indicators")
let heroCarouselItems=select('#heroCarousel .carousel-item',true)
heroCarouselItems.forEach((item,index)=>{(index===0)?heroCarouselIndicators.innerHTML+="<li data-bs-target='#heroCarousel' data-bs-slide-to='"+index+"' class='active'></li>":heroCarouselIndicators.innerHTML+="<li data-bs-target='#heroCarousel' data-bs-slide-to='"+index+"'></li>"});let backtotop=select('.back-to-top')
if(backtotop){const toggleBacktotop=()=>{if(window.scrollY>100){backtotop.classList.add('active')}else{backtotop.classList.remove('active')}}
window.addEventListener('load',toggleBacktotop)
onscroll(document,toggleBacktotop)}
on('click','.mobile-nav-toggle',function(e){select('#navbar').classList.toggle('navbar-mobile')
this.classList.toggle('bi-list')
this.classList.toggle('bi-x')})
on('click','.navbar .dropdown > a',function(e){if(select('#navbar').classList.contains('navbar-mobile')){e.preventDefault()
this.nextElementSibling.classList.toggle('dropdown-active')}},true)
on('click','.scrollto',function(e){if(select(this.hash)){e.preventDefault()
let navbar=select('#navbar')
if(navbar.classList.contains('navbar-mobile')){navbar.classList.remove('navbar-mobile')
let navbarToggle=select('.mobile-nav-toggle')
navbarToggle.classList.toggle('bi-list')
navbarToggle.classList.toggle('bi-x')}
scrollto(this.hash)}},true)
window.addEventListener('load',()=>{if(window.location.hash){if(select(window.location.hash)){scrollto(window.location.hash)}}});let preloader=select('#preloader');if(preloader){window.addEventListener('load',()=>{preloader.remove()});}
let skilsContent=select('.skills-content');if(skilsContent){new Waypoint({element:skilsContent,offset:'80%',handler:function(direction){let progress=select('.progress .progress-bar',true);progress.forEach((el)=>{el.style.width=el.getAttribute('aria-valuenow')+'%'});}})}
window.addEventListener('load',()=>{let portfolioContainer=select('.portfolio-container');if(portfolioContainer){let portfolioIsotope=new Isotope(portfolioContainer,{itemSelector:'.portfolio-item',layoutMode:'fitRows'});let portfolioFilters=select('#portfolio-flters li',true);on('click','#portfolio-flters li',function(e){e.preventDefault();portfolioFilters.forEach(function(el){el.classList.remove('filter-active');});this.classList.add('filter-active');portfolioIsotope.arrange({filter:this.getAttribute('data-filter')});portfolioIsotope.on('arrangeComplete',function(){AOS.refresh()});},true);}});const portfolioLightbox=GLightbox({selector:'.portfolio-lightbox'});new Swiper('.portfolio-details-slider',{speed:400,loop:true,autoplay:{delay:5000,disableOnInteraction:false},pagination:{el:'.swiper-pagination',type:'bullets',clickable:true}});new Swiper('.clients-slider',{speed:400,loop:true,autoplay:{delay:5000,disableOnInteraction:false},slidesPerView:'auto',pagination:{el:'.swiper-pagination',type:'bullets',clickable:true},breakpoints:{320:{slidesPerView:2,spaceBetween:20},480:{slidesPerView:3,spaceBetween:20},640:{slidesPerView:4,spaceBetween:20},992:{slidesPerView:6,spaceBetween:20}}});new Swiper('.testimonials-slider',{speed:600,loop:true,autoplay:{delay:5000,disableOnInteraction:false},slidesPerView:'auto',pagination:{el:'.swiper-pagination',type:'bullets',clickable:true}});window.addEventListener('load',()=>{AOS.init({duration:1000,easing:'ease-in-out',once:true,mirror:false})});new PureCounter();})();$(document).ready(function(){$(".preloader").hide();$("#MainForm").on("submit",function(){$(".preloader").fadeIn();});});function logoutFunction(){swal.fire({title:"Sure Want to Logout ?",type:"warning",showCancelButton:true,confirmButtonColor:"#3085d6",cancelButtonColor:"#d33",confirmButtonText:"OK",closeOnConfirm:true,closeOnCancel:false,}).then((result)=>{if(result.value===true){$("#logoutform").submit();}});}
function confirmFunction(){event.preventDefault();var form=event.target.form;Swal.fire({title:"Are you sure?",text:"Want to logout!",type:"warning",showCancelButton:true,confirmButtonColor:"#f00000",cancelButtonColor:"#333",confirmButtonText:"Yes,Logout!",}).then((result)=>{if(result.value){form.submit();}});}
var navItems=document.querySelectorAll(".bloc-icon");navItems.forEach(function(e,i){e.addEventListener("click",function(e){navItems.forEach(function(e2,i2){e2.classList.remove("block-icon-active");});this.classList.add("block-icon-active");});});(function(){"use strict";var tooltipTriggerList=[].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));tooltipTriggerList.forEach(function(tooltipTriggerEl){new bootstrap.Tooltip(tooltipTriggerEl);});})();$(document).ready(function(){$("#sidebarCollapse").on("click",function(){$("#sidebar").addClass("active");});$("#sidebarCollapseX").on("click",function(){$("#sidebar").removeClass("active");});$("#sidebarCollapse").on("click",function(){if($("#sidebar").hasClass("active")){$(".overlay").addClass("visible");console.log("it's working!");}});$("#sidebarCollapseX").on("click",function(){$(".overlay").removeClass("visible");});});var tooltipTriggerList=[].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));var tooltipList=tooltipTriggerList.map(function(tooltipTriggerEl){return new bootstrap.Tooltip(tooltipTriggerEl);});document.addEventListener("DOMContentLoaded",function(){window.addEventListener("scroll",function(){if(window.scrollY>50){document.getElementById("navbar_top").classList.add("is-scrolling");navbar_height=document.querySelector(".navbar").offsetHeight;document.body.style.paddingTop=navbar_height+"px";}else{document.getElementById("navbar_top").classList.remove("is-scrolling");document.body.style.paddingTop="0";}});});(function(window,$,undefined){"use strict";$(document).ready(function(){function is_scrolling(){var $element=$(".site-header"),$nav_height=$element.outerHeight(true);if($(this).scrollTop()>=$nav_height){$element.addClass("is-scrolling");}else{$element.removeClass("is-scrolling");}}
$(window).scroll(_.throttle(is_scrolling,200));});})(this,jQuery);(function(){"use strict";var forms=document.querySelectorAll(".needs-validation");Array.prototype.slice.call(forms).forEach(function(form){form.addEventListener("submit",function(event){if(!form.checkValidity()){event.preventDefault();event.stopPropagation();}
form.classList.add("was-validated");},false);});})();;