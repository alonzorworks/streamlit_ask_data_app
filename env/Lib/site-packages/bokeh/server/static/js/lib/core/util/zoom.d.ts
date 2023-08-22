import type { Interval } from "../types";
import type { Scale } from "../../models/scales/scale";
type Bounds = [number, number];
type Scales = Map<string, Scale>;
type Intervals = Map<string, Interval>;
export type ScaleRanges = {
    xrs: Intervals;
    yrs: Intervals;
    factor: number;
};
export declare function scale_highlow(range: Interval, factor: number, center?: number | null): Bounds;
export declare function get_info(scales: Scales, [sxy0, sxy1]: Bounds): Intervals;
export declare function scale_range(x_scales: Scales, y_scales: Scales, x_range: Interval, y_range: Interval, factor: number, x_axis?: boolean, y_axis?: boolean, center?: {
    x?: number | null;
    y?: number | null;
} | null): ScaleRanges;
export {};
//# sourceMappingURL=zoom.d.ts.map