import type { Transform } from "./base";
import type { LineGLVisuals } from "./base_line";
import { BaseLineGL } from "./base_line";
import type { Uint8Buffer } from "./buffer";
import type { ReglWrapper } from "./regl_wrap";
import type { StepView } from "../step";
export declare class StepGL extends BaseLineGL {
    readonly glyph: StepView;
    constructor(regl_wrapper: ReglWrapper, glyph: StepView);
    draw(indices: number[], main_glyph: StepView, transform: Transform): void;
    protected _get_show_buffer(_indices: number[], main_gl_glyph: StepGL): Uint8Buffer;
    protected _get_visuals(): LineGLVisuals;
    protected _set_data_points(): Float32Array;
}
//# sourceMappingURL=step.d.ts.map