/**
 * @module PostStateMachine
 * @description State machine for post lifecycle transitions.
 * States: brain_dump → refined → tailored → queued → scheduled → posted → tracked
 */
export class PostStateMachine {
  static STATES = {
    BRAIN_DUMP: 'brain_dump',
    REFINED: 'refined',
    TAILORED: 'tailored',
    QUEUED: 'queued',
    SCHEDULED: 'scheduled',
    POSTED: 'posted',
    TRACKED: 'tracked',
  };

  static TRANSITIONS = {
    brain_dump: ['refined'],
    refined: ['tailored', 'brain_dump'],
    tailored: ['queued', 'refined'],
    queued: ['scheduled', 'tailored'],
    scheduled: ['posted', 'queued'],
    posted: ['tracked'],
    tracked: [],
  };

  /**
   * Check if a transition is valid.
   * @param {string} from
   * @param {string} to
   * @returns {boolean}
   */
  static canTransition(from, to) {
    return (PostStateMachine.TRANSITIONS[from] || []).includes(to);
  }

  /**
   * Perform a transition or throw if invalid.
   * @param {string} currentState
   * @param {string} targetState
   * @returns {string} The new state
   */
  static transition(currentState, targetState) {
    if (!PostStateMachine.canTransition(currentState, targetState)) {
      throw new Error(`Invalid transition: ${currentState} → ${targetState}`);
    }
    return targetState;
  }

  /** @returns {string[]} All valid states */
  static getAllStates() {
    return Object.values(PostStateMachine.STATES);
  }
}

export default PostStateMachine;
