"""Optional demonstration alerts. Does not modify the frozen research policy."""
import copy
import math
from .policy import TemporalPolicy


class YawnDemoAlert:
    def __init__(self, threshold=.7, hold_s=1., max_gap_s=.6):
        self.config = {'version': 'demo-yawn-v1', 'threshold': threshold,
                       'hold_s': hold_s, 'max_gap_s': max_gap_s,
                       'validated': False}
        self.policy = TemporalPolicy({'min_score': threshold, 'max_gap_s': max_gap_s,
                                      'hold_s': {'yawning': hold_s}})

    def update(self, result):
        prediction = result['predictions'].get('yawn')
        score = None
        if prediction is not None:
            probs = prediction['probabilities']
            values = [probs.get(k) for k in ('no_yawn', 'yawning_with_hand', 'yawning_without_hand')]
            if all(isinstance(v, (int, float)) and math.isfinite(v) and 0 <= v <= 1 for v in values):
                if abs(sum(values)-1) <= 1e-4:
                    score = values[1] + values[2]
        signals = {'yawning': None if score is None else score >= self.config['threshold']}
        extra = self.policy.update(result['timestamp_s'], signals)
        merged = copy.deepcopy(result)
        merged['research_alerts'] = copy.deepcopy(result['alerts'])
        for key in ('active', 'started', 'ended', 'unknown'):
            merged['alerts'][key] = sorted(set(result['alerts'][key]) | set(extra[key]))
        alerts = merged['alerts']
        alerts['status'] = 'warning' if alerts['active'] else ('unknown' if alerts['unknown'] else 'no_active_warning')
        merged['demo_yawn'] = {'config': self.config, 'score': score, 'signal': signals['yawning']}
        return merged
