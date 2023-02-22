def grid_search(model, param_grid, ens=False):
    val = 10
    grid_search = GridSearchCV(model, param_grid, cv=kfold, scoring='neg_mean_squared_error', n_jobs=4)
    grid_search.fit(X, y_log)
    bestestimator = grid_search.best_estimator_ 
    bestscore= np.sqrt(-grid_search.best_score_) 
    bestparams= grid_search.best_params_
    if not ens:
        return bestestimator, bestscore
    else:
        return bestparams, bestscore


def cv_rmse(model):
    scores_rmse = np.sqrt(-cross_val_score(model, X, y_log, scoring="neg_mean_squared_error", cv=kfold, n_jobs=4))
    mean_rmse = scores_rmse.mean()
    std_rmse = scores_rmse.std()
    return mean_rmse, std_rmse


def isSubsequence(self, s: str, t: str) -> bool:
    if len(s)==0:
        return True
    if len(t)<len(s):
        return False
    index = 0
    for each_char in t:
        if each_char == s[index]:
            index+=1
            if index==len(s):
                return True
    return False