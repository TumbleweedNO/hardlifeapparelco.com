import { useState, useEffect, useRef } from "react";

const HRDLFHomepage = () => {
  const [visible, setVisible] = useState({});
  const observers = useRef([]);

  useEffect(() => {
    const sections = document.querySelectorAll("[data-animate]");
    sections.forEach((el) => {
      const obs = new IntersectionObserver(
        ([entry]) => {
          if (entry.isIntersecting) {
            setVisible((v) => ({ ...v, [el.dataset.animate]: true }));
          }
        },
        { threshold: 0.1 }
      );
      obs.observe(el);
      observers.current.push(obs);
    });
    return () => observers.current.forEach((o) => o.disconnect());
  }, []);

  const fadeIn = (id) => ({
    opacity: visible[id] ? 1 : 0,
    transform: visible[id] ? "translateY(0)" : "translateY(30px)",
    transition: "opacity 0.8s ease, transform 0.8s ease",
  });

  // Greenhouse image as base64-encoded placeholder (dark green moody tones)
  const greenhouseBg = "linear-gradient(180deg, #2a3d2a 0%, #1a2e1a 20%, #0d1f12 45%, #162a18 65%, #0a1a0e 85%, #0a0f0a 100%)";

  return (
    <div style={{ fontFamily: "'Helvetica Neue', Arial, sans-serif", color: "#0A0A0A", background: "#FAFAFA", minHeight: "100vh" }}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@400;500;700&display=swap');
        * { box-sizing: border-box; margin: 0; padding: 0; }
        @keyframes ticker { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
        .card-hover { transition: transform 0.4s ease, box-shadow 0.4s ease; }
        .card-hover:hover { transform: translateY(-4px); box-shadow: 0 12px 40px rgba(0,0,0,0.12); }
        .btn-hover { transition: all 0.3s ease; cursor: pointer; }
        .btn-hover:hover { transform: translateY(-1px); opacity: 0.9; }
      `}</style>

      {/* NAV */}
      <nav style={{ display: "flex", alignItems: "center", justifyContent: "space-between", padding: "0 clamp(16px, 4vw, 48px)", height: 72, background: "#FAFAFA", borderBottom: "1px solid #E8E8E8", position: "sticky", top: 0, zIndex: 100 }}>
        <div style={{ fontFamily: "'Bebas Neue', Impact, sans-serif", fontSize: 30, letterSpacing: 2 }}>HRDLF<span style={{ color: "#FF2D2D" }}>.</span></div>
        <div style={{ display: "flex", gap: "clamp(12px, 2.5vw, 36px)", alignItems: "center", fontSize: 11, letterSpacing: 2.5, textTransform: "uppercase", fontFamily: "'DM Sans', sans-serif", fontWeight: 500 }}>
          <span style={{ color: "#404040" }}>About</span>
          <span style={{ color: "#404040" }}>Editorial</span>
          <span style={{ color: "#404040" }}>Lookbook</span>
          <span style={{ color: "#404040" }}>Press</span>
          <div className="btn-hover" style={{ background: "#0A0A0A", color: "#fff", padding: "10px 22px", fontSize: 11, letterSpacing: 2, fontWeight: 600 }}>SHOP NOW →</div>
        </div>
      </nav>

      {/* HERO IMAGE — Full bleed, sits directly below nav */}
      <div style={{
        width: "100%",
        height: "75vh",
        background: greenhouseBg,
        position: "relative",
        overflow: "hidden",
      }}>
        {/* Atmospheric texture layers to simulate the greenhouse photo */}
        <div style={{ position: "absolute", inset: 0, background: "radial-gradient(ellipse at 50% 35%, rgba(100,140,90,0.3) 0%, transparent 55%)" }} />
        <div style={{ position: "absolute", inset: 0, background: "radial-gradient(ellipse at 35% 55%, rgba(70,100,65,0.2) 0%, transparent 45%)" }} />
        <div style={{ position: "absolute", inset: 0, background: "radial-gradient(ellipse at 65% 60%, rgba(50,80,55,0.15) 0%, transparent 40%)" }} />
        
        {/* Glass pane lines */}
        <div style={{ position: "absolute", top: 0, left: "22%", width: 1, height: "100%", background: "rgba(255,255,255,0.04)" }} />
        <div style={{ position: "absolute", top: 0, left: "50%", width: 1, height: "100%", background: "rgba(255,255,255,0.03)" }} />
        <div style={{ position: "absolute", top: 0, left: "78%", width: 1, height: "100%", background: "rgba(255,255,255,0.04)" }} />
        <div style={{ position: "absolute", top: "30%", left: 0, width: "100%", height: 1, background: "rgba(255,255,255,0.03)" }} />
        
        {/* Silhouette hint - center figure */}
        <div style={{
          position: "absolute", bottom: 0, left: "50%", transform: "translateX(-50%)",
          width: 160, height: "72%",
          background: "linear-gradient(to top, rgba(0,0,0,0.25) 0%, rgba(0,0,0,0.12) 50%, transparent 85%)",
          borderRadius: "40% 40% 0 0",
        }} />

        {/* "HardLife" on the tee - ghost text */}
        <div style={{
          position: "absolute", top: "42%", left: "50%", transform: "translateX(-50%)",
          fontFamily: "'Cormorant Garamond', Georgia, serif",
          fontSize: 14, color: "rgba(255,255,255,0.08)", letterSpacing: 4, fontStyle: "italic",
        }}>HardLife</div>

        {/* Corner label */}
        <div style={{
          position: "absolute", bottom: 24, right: 32,
          fontSize: 10, letterSpacing: 3, textTransform: "uppercase",
          color: "rgba(255,255,255,0.25)", fontFamily: "'DM Sans', sans-serif",
        }}>Spring 2026 Collection</div>
      </div>

      {/* HERO TEXT — Below the image */}
      <section style={{ background: "#0A0A0A", color: "#fff", padding: "64px clamp(20px, 4vw, 48px) 80px" }}>
        <div style={{ maxWidth: 1400, margin: "0 auto" }}>
          <div style={{ fontSize: 11, letterSpacing: 3.5, textTransform: "uppercase", color: "rgba(255,255,255,0.5)", marginBottom: 28, display: "flex", alignItems: "center", gap: 14, fontFamily: "'DM Sans', sans-serif" }}>
            <div style={{ width: 32, height: 2, background: "#FF2D2D" }} />
            Est. 2006 — Philadelphia, PA
          </div>
          
          <div style={{ display: "grid", gridTemplateColumns: "1.4fr 1fr", gap: "clamp(40px, 6vw, 100px)", alignItems: "end" }}>
            <div>
              <h1 style={{ fontFamily: "'Bebas Neue', Impact, sans-serif", fontSize: "clamp(48px, 7.5vw, 96px)", lineHeight: 0.92, letterSpacing: -1, textTransform: "uppercase" }}>
                There Is Only One.<br /><span style={{ color: "#FF2D2D" }}>The Original.</span>
              </h1>
            </div>
            <div>
              <p style={{ color: "rgba(255,255,255,0.55)", fontSize: 16, lineHeight: 1.8, marginBottom: 32, fontFamily: "'Cormorant Garamond', Georgia, serif", fontStyle: "italic" }}>
                Hardlife Apparel Company LTD was born in 2006 from skateboard culture and the belief that nothing worth having comes without the grind. Nearly two decades later, the mission hasn't changed.
              </p>
              <div style={{ display: "flex", gap: 16, flexWrap: "wrap" }}>
                <div className="btn-hover" style={{ background: "#fff", color: "#0A0A0A", padding: "14px 32px", fontSize: 11, letterSpacing: 2.5, textTransform: "uppercase", fontWeight: 700, fontFamily: "'DM Sans', sans-serif" }}>Shop the Collection →</div>
                <div className="btn-hover" style={{ border: "1px solid rgba(255,255,255,0.35)", color: "#fff", padding: "14px 32px", fontSize: 11, letterSpacing: 2.5, textTransform: "uppercase", fontWeight: 500, fontFamily: "'DM Sans', sans-serif" }}>Our Story</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* TICKER */}
      <div style={{ background: "#0A0A0A", overflow: "hidden", padding: "14px 0", borderTop: "1px solid #1a1a1a" }}>
        <div style={{ display: "flex", animation: "ticker 30s linear infinite", whiteSpace: "nowrap" }}>
          {[...Array(2)].map((_, j) => (
            <div key={j} style={{ display: "flex", alignItems: "center", gap: 48, paddingRight: 48 }}>
              {["Hardlife Apparel Company LTD", "·", "Est. 2006", "·", "Nothing Awesome Comes Easy", "·", "HRDLF", "·", "The Original Since 2006", "·"].map((text, i) => (
                <span key={i} style={{ fontFamily: "'Bebas Neue', Impact, sans-serif", fontSize: 48, color: "rgba(255,255,255,0.04)", textTransform: "uppercase", letterSpacing: 3 }}>{text}</span>
              ))}
            </div>
          ))}
        </div>
      </div>

      {/* BRAND MISSION */}
      <section data-animate="mission" style={{ padding: "100px clamp(20px, 4vw, 48px)", maxWidth: 1400, margin: "0 auto", ...fadeIn("mission") }}>
        <div style={{ display: "grid", gridTemplateColumns: "1.2fr 1fr", gap: "clamp(40px, 6vw, 80px)", alignItems: "center" }}>
          <div>
            <div style={{ fontSize: 11, letterSpacing: 3.5, textTransform: "uppercase", color: "#FF2D2D", marginBottom: 18, display: "flex", alignItems: "center", gap: 14, fontFamily: "'DM Sans', sans-serif" }}>
              <div style={{ width: 32, height: 2, background: "#FF2D2D" }} />
              Brand Heritage
            </div>
            <h2 style={{ fontFamily: "'Bebas Neue', Impact, sans-serif", fontSize: "clamp(36px, 4vw, 56px)", lineHeight: 0.95, textTransform: "uppercase", marginBottom: 28 }}>
              Built Different<br /><span style={{ color: "#FF2D2D" }}>Since Day One.</span>
            </h2>
            <p style={{ color: "#555", fontSize: 15, lineHeight: 1.85, marginBottom: 18, fontFamily: "'DM Sans', sans-serif" }}>
              While other brands chase trends, Hardlife Apparel Company has been building culture from the ground up since 2006. Born in Philadelphia's skateboard scene, HRDLF represents the grind, the grit, and the relentless pursuit of authenticity.
            </p>
            <p style={{ color: "#555", fontSize: 15, lineHeight: 1.85, fontFamily: "'DM Sans', sans-serif" }}>
              Nearly two decades of independence. Zero outside investors. One uncompromising vision.
            </p>
          </div>
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 20 }}>
            {[{ number: "2006", label: "Year Founded" }, { number: "19", label: "Years Independent" }, { number: "PHL", label: "Philadelphia Origin" }, { number: "1", label: "The Only Original" }].map((stat, i) => (
              <div key={i} style={{ background: "#F5F3EF", padding: "36px 20px", textAlign: "center" }}>
                <div style={{ fontFamily: "'Bebas Neue', Impact, sans-serif", fontSize: 42, lineHeight: 1, marginBottom: 10 }}>{stat.number}</div>
                <div style={{ fontSize: 10, letterSpacing: 2.5, textTransform: "uppercase", color: "#808080", fontFamily: "'DM Sans', sans-serif" }}>{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* COLLECTION */}
      <section data-animate="collection" style={{ padding: "80px clamp(20px, 4vw, 48px) 100px", background: "#F5F3EF", ...fadeIn("collection") }}>
        <div style={{ maxWidth: 1400, margin: "0 auto" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-end", marginBottom: 48 }}>
            <div>
              <div style={{ fontSize: 11, letterSpacing: 3.5, textTransform: "uppercase", color: "#FF2D2D", marginBottom: 18, display: "flex", alignItems: "center", gap: 14, fontFamily: "'DM Sans', sans-serif" }}>
                <div style={{ width: 32, height: 2, background: "#FF2D2D" }} />The Collection
              </div>
              <h2 style={{ fontFamily: "'Bebas Neue', Impact, sans-serif", fontSize: "clamp(36px, 4vw, 56px)", lineHeight: 0.95, textTransform: "uppercase" }}>Premium<br /><span style={{ color: "#FF2D2D" }}>Streetwear.</span></h2>
            </div>
            <div className="btn-hover" style={{ fontSize: 11, letterSpacing: 2, textTransform: "uppercase", borderBottom: "1px solid #0A0A0A", paddingBottom: 4, fontFamily: "'DM Sans', sans-serif" }}>View All →</div>
          </div>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: 24 }}>
            {[
              { tag: "Classic Collection", title: "Old English Tee & Accessories", desc: "Premium heavyweight cotton with Old English branding and the iconic skull and laurel beanie.", bg: "linear-gradient(135deg, #1a2e1a, #2a3a2a)" },
              { tag: "Hoodies", title: "HardLife Old English Hoodie", desc: "Not just a brand. A lifestyle. Signature Old English hoodie in premium heavyweight fleece.", bg: "linear-gradient(135deg, #0e0e1e, #1a1a2e)" },
              { tag: "Accessories", title: "HRDLF Bags & Caps", desc: "Camo drawstring with skull and laurel logo, plus the HRDLF snapback in signature red.", bg: "linear-gradient(135deg, #2a1a1a, #1e1412)" },
            ].map((item, i) => (
              <div key={i} className="card-hover" style={{ background: "#fff", overflow: "hidden" }}>
                <div style={{ background: item.bg, height: 260, display: "flex", alignItems: "center", justifyContent: "center" }}>
                  <div style={{ fontFamily: "'Bebas Neue', Impact, sans-serif", fontSize: 24, color: "rgba(255,255,255,0.07)", textTransform: "uppercase", letterSpacing: 6 }}>HRDLF</div>
                </div>
                <div style={{ padding: "22px 20px 26px" }}>
                  <div style={{ fontSize: 10, letterSpacing: 2.5, textTransform: "uppercase", color: "#FF2D2D", marginBottom: 10, fontFamily: "'DM Sans', sans-serif" }}>{item.tag}</div>
                  <h3 style={{ fontFamily: "'Bebas Neue', Impact, sans-serif", fontSize: 21, letterSpacing: 1, marginBottom: 10 }}>{item.title}</h3>
                  <p style={{ color: "#666", fontSize: 13, lineHeight: 1.7, fontFamily: "'DM Sans', sans-serif" }}>{item.desc}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section data-animate="cta" style={{ background: "#0A0A0A", color: "#fff", padding: "80px clamp(20px, 4vw, 48px)", textAlign: "center", ...fadeIn("cta") }}>
        <h2 style={{ fontFamily: "'Bebas Neue', Impact, sans-serif", fontSize: "clamp(36px, 5vw, 64px)", textTransform: "uppercase", marginBottom: 16, lineHeight: 0.95 }}>
          Nothing Awesome<br /><span style={{ color: "#FF2D2D" }}>Comes Easy.</span>
        </h2>
        <p style={{ color: "#999", fontSize: 17, marginBottom: 36, fontFamily: "'Cormorant Garamond', Georgia, serif", fontStyle: "italic" }}>Join the movement. Wear the grind.</p>
        <div className="btn-hover" style={{ display: "inline-block", background: "#fff", color: "#0A0A0A", padding: "16px 48px", fontSize: 12, letterSpacing: 2.5, textTransform: "uppercase", fontWeight: 700, fontFamily: "'DM Sans', sans-serif" }}>Shop HRDLF →</div>
      </section>

      {/* FOOTER */}
      <footer style={{ background: "#0A0A0A", color: "#fff", padding: "60px clamp(20px, 4vw, 48px) 30px", borderTop: "1px solid #1a1a1a" }}>
        <div style={{ maxWidth: 1400, margin: "0 auto" }}>
          <div style={{ display: "grid", gridTemplateColumns: "2fr 1fr 1fr 1fr", gap: 48, marginBottom: 48 }}>
            <div>
              <div style={{ fontFamily: "'Bebas Neue', Impact, sans-serif", fontSize: 36, letterSpacing: 2, marginBottom: 8 }}>HRDLF<span style={{ color: "#FF2D2D" }}>.</span></div>
              <p style={{ fontFamily: "'Cormorant Garamond', Georgia, serif", fontSize: 15, fontStyle: "italic", color: "#999", marginBottom: 12 }}>Nothing Awesome Comes Easy.</p>
              <p style={{ fontSize: 13, color: "#666", fontFamily: "'DM Sans', sans-serif", lineHeight: 1.6 }}>Hardlife Apparel Company LTD.<br />Founded in Philadelphia in 2006.</p>
            </div>
            {[{ title: "Navigate", links: ["Home", "About", "Editorial", "Lookbook", "Press"] }, { title: "Shop", links: ["T-Shirts", "Hoodies", "Accessories"] }, { title: "Connect", links: ["Instagram", "TikTok", "X / Twitter"] }].map((col, i) => (
              <div key={i}>
                <div style={{ fontSize: 11, letterSpacing: 2.5, textTransform: "uppercase", marginBottom: 20, fontFamily: "'DM Sans', sans-serif", fontWeight: 700 }}>{col.title}</div>
                {col.links.map((link, j) => <div key={j} style={{ fontSize: 14, color: "#888", marginBottom: 12, fontFamily: "'DM Sans', sans-serif" }}>{link}</div>)}
              </div>
            ))}
          </div>
          <div style={{ borderTop: "1px solid #1a1a1a", paddingTop: 24, display: "flex", justifyContent: "space-between" }}>
            <div style={{ fontSize: 12, color: "#555", fontFamily: "'DM Sans', sans-serif" }}>© 2026 Hardlife Apparel Company LTD. All rights reserved.</div>
            <div style={{ display: "flex", gap: 20, fontSize: 12, color: "#666", fontFamily: "'DM Sans', sans-serif" }}><span>IG</span><span>TT</span><span>X</span></div>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default HRDLFHomepage;
