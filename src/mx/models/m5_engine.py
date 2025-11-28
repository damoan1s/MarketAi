# -----------------------------------------------
# M5 — Dual Market Intention Engine
# Detects divergence between Futures vs Spot
# and extracts the true institutional intention.
# -----------------------------------------------

class M5Engine:

    def init(self):
        pass

    def compute_range(self, high, low):
        """Return HH - LL movement."""
        return high - low

    def divergence(self, fut_range, spot_range):
        """Return absolute and percentage divergence."""
        diff = fut_range - spot_range
        pct = (diff / spot_range) * 100 if spot_range != 0 else 0
        return diff, pct

    def wick_pattern(self, fut_wick, spot_wick):
        """Detect wick asymmetry between markets."""
        if fut_wick > spot_wick:
            return "futures_aggressive"
        elif spot_wick > fut_wick:
            return "spot_aggressive"
        return "neutral"

    def angle_shift(self, fut_angle, spot_angle):
        """Determine which market drives the structural angle."""
        if fut_angle > spot_angle:
            return "future_drives"
        elif spot_angle > fut_angle:
            return "spot_drives"
        return "aligned"

    def detect_intent(self, fut_data, spot_data):
        """
        fut_data & spot_data example:
        {
            'high': float,
            'low': float,
            'wick': float,
            'angle': float
        }
        """

        fut_range = self.compute_range(fut_data['high'], fut_data['low'])
        spot_range = self.compute_range(spot_data['high'], spot_data['low'])

        diff, pct = self.divergence(fut_range, spot_range)
        wick_state = self.wick_pattern(fut_data['wick'], spot_data['wick'])
        angle_state = self.angle_shift(fut_data['angle'], spot_data['angle'])

        # ---- Decision Logic ----

        # Case 1: Futures stronger + sharper angle + bigger wick
        if diff > 0 and wick_state == "futures_aggressive" and angle_state == "future_drives":
            return {
                "intent": "sell_coming",
                "reason": "Futures pushing aggressively while spot resists."
            }

        # Case 2: Spot stronger + sharper angle + bigger wick
        if diff < 0 and wick_state == "spot_aggressive" and angle_state == "spot_drives":
            return {
                "intent": "buy_coming",
                "reason": "Spot leading the structure while futures lag."
            }

        # Case 3: Wick asymmetry indicates liquidity grab
        if wick_state == "futures_aggressive":
            return {
                "intent": "liquidity_hunt_future_side",
                "reason": "Futures showing wick imbalance."
            }

        if wick_state == "spot_aggressive":
            return {
                "intent": "liquidity_hunt_spot_side",
                "reason": "Spot showing wick imbalance."
            }

        # Case 4: Markets are aligned (neutral)
        return {
            "intent": "neutral",
            "reason": "No significant divergence."
        }
