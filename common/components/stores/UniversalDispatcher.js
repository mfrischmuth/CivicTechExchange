// @flow

"use strict";

import type { MyProjectsActionType } from "./MyProjectsStore.js";
import type { MyGroupsActionType } from "./MyGroupsStore.js";
import type { NavigationActionType } from "./NavigationStore.js";
import type { OffsetActionType } from "./PageOffsetStore.js";
import type { LinkListActionType } from "./LinkListStore.js";
import { Dispatcher } from "flux";

type UniversalActionType =
  | MyProjectsActionType
  | MyGroupsActionType
  | NavigationActionType
  | OffsetActionType
  | LinkListActionType;

const UniversalDispatcher: Dispatcher<UniversalActionType> = new Dispatcher();

export default UniversalDispatcher;
