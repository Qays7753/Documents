#!/bin/bash
# Micro Bold Modular — Agent-03 systematic screenshot evidence generator
set -e
PROTO="/home/z/my-project/repos/Micro-Bold-Modular-Design-Handoff-V1/agent-runs/agent-03-multi-agent/prototype"
OUT="/home/z/my-project/repos/Micro-Bold-Modular-Design-Handoff-V1/agent-runs/agent-03-multi-agent/screenshots"
mkdir -p "$OUT"

shot() { # shot <url> <name> <w> <h>
  agent-browser set viewport "$3" "$4" >/dev/null 2>&1
  agent-browser open "$1" >/dev/null 2>&1
  sleep 0.6
  agent-browser screenshot "$OUT/$2.png" >/dev/null 2>&1
  echo "✓ $2"
}

DIRS=(c1-warm-bold c2-confident-bold c3-dynamic-modular)

for d in "${DIRS[@]}"; do
  # home states, light, 390
  shot "file://$PROTO/$d/home.html" "$d-home-positive-light-390" 390 844
  shot "file://$PROTO/$d/home.html?state=incomplete" "$d-home-incomplete-light-390" 390 844
  shot "file://$PROTO/$d/home.html?state=negative" "$d-home-negative-light-390" 390 844
  shot "file://$PROTO/$d/home.html?state=empty" "$d-home-empty-light-390" 390 844
  # dark mode home (positive + incomplete)
  shot "file://$PROTO/$d/home.html?theme=dark" "$d-home-positive-dark-390" 390 844
  shot "file://$PROTO/$d/home.html?state=incomplete&theme=dark" "$d-home-incomplete-dark-390" 390 844
  # sale flow
  shot "file://$PROTO/$d/sale.html" "$d-sale-form-light-390" 390 844
  shot "file://$PROTO/$d/sale.html?state=validation" "$d-sale-validation-light-390" 390 844
  shot "file://$PROTO/$d/sale.html?state=success" "$d-sale-success-light-390" 390 844
  shot "file://$PROTO/$d/sale.html?state=system-error" "$d-sale-syserror-light-390" 390 844
  # other screens
  shot "file://$PROTO/$d/finance.html" "$d-finance-light-390" 390 844
  shot "file://$PROTO/$d/work.html" "$d-work-light-390" 390 844
  shot "file://$PROTO/$d/tools.html" "$d-tools-light-390" 390 844
  shot "file://$PROTO/$d/tools.html?theme=dark" "$d-tools-dark-390" 390 844
  shot "file://$PROTO/$d/market.html" "$d-market-light-390" 390 844
  shot "file://$PROTO/$d/products.html" "$d-products-light-390" 390 844
  shot "file://$PROTO/$d/order.html" "$d-order-light-390" 390 844
  shot "file://$PROTO/$d/more.html" "$d-more-light-390" 390 844
  # responsive proofs on critical screens (positive home + success)
  shot "file://$PROTO/$d/home.html" "$d-home-positive-light-320" 320 700
  shot "file://$PROTO/$d/home.html" "$d-home-positive-light-430" 430 900
  shot "file://$PROTO/$d/sale.html?state=success" "$d-sale-success-light-320" 320 700
  shot "file://$PROTO/$d/sale.html?state=success" "$d-sale-success-light-430" 430 900
  # 200% text stress (positive home) + reduced motion marker (sale success)
  shot "file://$PROTO/$d/home.html?zoom=200" "$d-home-positive-light-390-zoom200" 390 844
  shot "file://$PROTO/$d/sale.html?state=success&motion=reduce" "$d-sale-success-light-390-reducedmotion" 390 844
  # menu sheet from logo
  shot "file://$PROTO/$d/home.html?sheet=menu" "$d-home-menu-light-390" 390 844
done

echo "--- done: $(ls "$OUT" | wc -l) screenshots ---"
