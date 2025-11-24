# Conditions.md

## DNA 2.0 — Institutional Market Cycle Engine

### 1) Introduction:
MarketAI is built on the DNA 2.0 framework, which aims to understand institutional market movements. This framework is based on behavioral indicators that can help us identify market intent before the movement occurs. Below, we outline the key conditions that drive this market behavior.

### 2) Core Inputs:

1. Spot / Futures Delta:
   - This measures the difference between the Spot price and the Futures price. A significant delta indicates institutional involvement, either in absorption or accumulation.
   
2. CVD — Cumulative Volume Delta:
   - This measures the change in volume between the bid and ask sides of the market. Positive CVD indicates buying pressure, while negative CVD signals selling pressure.

3. TVI — Trade Volume Index:
   - This index highlights market participation based on trade volume. An increase in volume typically signals a shift in market sentiment.

4. Volume Imbalance:
   - This measures the difference between buying and selling volume. A large imbalance suggests the market is being dominated by one side (buying or selling).

5. Liquidity Zones (Auto-detected):
   - These are the areas on the chart where liquidity is absorbed or released. Recognizing these zones allows us to predict upcoming market movements.

6. Volatility Compression:
   - A period where price movement contracts within a defined range. This typically precedes a sharp breakout in either direction.

7. Funding Rate Bias:
   - This refers to the difference between the funding rate of Futures contracts. A high funding rate bias suggests that one side (long or short) is being excessively leveraged, which often leads to a market reversal.

8. Orderbook Skew (OB):
   - This measures the imbalance in the orderbook between buy and sell orders. It provides insight into market sentiment and the pressure on prices.

---

### 3) Market Cycle — 5 Phases

1. Absorption (Phase 1):
   - In this phase, institutions absorb liquidity without causing major price movement. The market may see erratic price action as retail traders are triggered into action. CVD and Volume Imbalance indicate whether liquidity is being absorbed or not.

2. Exhaustion (Phase 2):
   - The trend shows signs of weakening. Volume diminishes, and market participants begin to lose confidence in the current direction. This is the phase of "tiredness," and markets often form consolidation patterns here.

3. Divergence (Phase 3):
   - At this stage, the Spot price and Futures prices diverge. The gap between the two markets suggests institutional intent. This is often followed by a strong directional move once the divergence is resolved.

4. Reversal (Phase 4):
   - The true institutional intent becomes visible. This phase marks a strong price movement in the opposite direction of the previous trend, signaling that institutions have begun their market action.

5. Expansion (Phase 5):
   - The market expands significantly, driven by institutional buying or selling. Price volatility is high, and the trend accelerates. Volume and liquidity are key indicators of whether this expansion is sustainable.

---

### 4) The DNA Score:
The DNA Score is calculated based on the following parameters:
- Spot / Futures Delta
- CVD (Cumulative Volume Delta)
- TVI (Trade Volume Index)
- Volume Imbalance
- Orderbook Skew
- Liquidity Zones
- Volatility Compression
- Funding Rate Bias

The DNA Score provides a real-time market reading, indicating the likelihood of a market shift.

---

### 5) Probability Engine:
The Probability Engine is used to calculate the likelihood of each market phase and its potential direction. Each phase (Absorption, Exhaustion, Divergence, Reversal, Expansion) gets a probability percentage based on historical data and current market behavior. This engine helps us estimate the risk and identify the most probable outcomes for a given market condition.

- Absorption: %P
- Exhaustion: %P
- Divergence: %P
- Reversal: %P
- Expansion: %P

---

### 6) Output System:
The Output System displays the calculated results from the DNA Engine and other tools in an intuitive and easy-to-understand format. It includes:

1. Cycle Radar: A semi-circle showing the market's current phase (Absorb / EXH / DIV / REV / EXP).
2. Heatmap of Pressure: Visual representation of areas of high or low market pressure.
3. Market State Label: The system labels the market's current state based on the DNA score, such as "Expansion" or "Reversal."

---

### 7) Automation Layer:
The Automation Layer includes semi-automated trading signals that assist with execution:

- Buy Signal (Phase 4 → 5)
- Sell Signal (Phase 2 → 3)
- Avoid Market (Phase 1)
- High-Risk Warning

These signals are based on real-time data, DNA scoring, and market behavior, helping users automate some aspects of their trading decisions.

---

### 8) Conclusion:
By understanding the market’s behavior through the DNA 2.0 Engine, MarketAI can predict future price movements and help traders make data-driven decisions. This framework is based on institutional behaviors that drive price action and liquidity. By tracking the market cycle and conditions outlined in this document, we are prepared to react to market changes and spot profitable opportunities.

---

End of Conditions.md
