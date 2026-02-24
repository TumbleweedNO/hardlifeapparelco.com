/* ============================================================
   HARDLIFE APPAREL COMPANY LTD — Site JavaScript
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  // — Mobile Nav Toggle —
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      nav.classList.toggle('is-open');
      toggle.classList.toggle('is-active');
    });
    nav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        nav.classList.remove('is-open');
        toggle.classList.remove('is-active');
      });
    });
  }

  // — Scroll-Based Fade In —
  const fadeEls = document.querySelectorAll('.fade-in, .stagger');
  if (fadeEls.length) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

    fadeEls.forEach(el => observer.observe(el));
  }

  // — Header Hide on Scroll Down, Show on Scroll Up —
  const header = document.querySelector('.site-header');
  let lastScroll = 0;
  if (header) {
    window.addEventListener('scroll', () => {
      const currentScroll = window.pageYOffset;
      if (currentScroll > 200) {
        if (currentScroll > lastScroll) {
          header.style.transform = 'translateY(-100%)';
        } else {
          header.style.transform = 'translateY(0)';
        }
      } else {
        header.style.transform = 'translateY(0)';
      }
      lastScroll = currentScroll;
    }, { passive: true });
  }

  // — Marquee Clone for Infinite Scroll —
  const marqueeInner = document.querySelector('.marquee__inner');
  if (marqueeInner) {
    marqueeInner.innerHTML += marqueeInner.innerHTML;
  }

  // — Year in Footer —
  const yearEl = document.querySelector('.js-year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

});
