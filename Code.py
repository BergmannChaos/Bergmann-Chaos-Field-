import chaos_field as cf

# Unstabilisiertes Chaos-Feld (divergiert bei γ → √8)
raw = cf.chaos_field_raw(gamma=2.5)
print(f"Unstabilisiert: {raw:.2e}")

# π-stabilisiertes Chaos-Feld (Fixpunkt ≈ 4.1888)
stable = cf.pi_stabilized_chaos(gamma=2.5)
print(f"π-stabilisiert: {stable:.6f}")

# π-modulierte effektive Hubble-Rate
H_classic = 67.4  # km/s/Mpc (CMB-Wert)
H_local   = cf.effective_hubble(H_classic, gamma=2.5, rho_grad=1e-9)
print(f"H_local ≈ {H_local:.1f} km/s/Mpc")

# π-modulierte Exzentrizität (für pyEFPE-Erweiterung)
e_eff = cf.pi_modulated_eccentricity(e0=0.20, gamma=2.5)
print(f"Effektive Exzentrizität: {e_eff:.4f}")
