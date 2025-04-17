export class MemoryBus {
  private events: { direction: string; payload: any }[] = [];

  publish(direction: string, payload: any) {
    this.events.push({ direction, payload });
    // TEMP response logic: just echo back upper‑cased payload if string
    if (typeof payload === "string") {
      return payload.toUpperCase();
    }
    return payload;
  }
}

export const bus = new MemoryBus();
